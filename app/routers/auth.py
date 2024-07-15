from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app import crud
from app.dependencies import get_redis
from app.models import EmailCode, Token, UserCreate, UserPublic
from app.utils import send_email
from app.utils.auth import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    authenticate_user,
    create_access_token,
)
from app.utils.result import Res
from fastapi import BackgroundTasks

from app.utils.send_email import generate_email

router = APIRouter(tags=["auth"], responses={404: {"description": "Not found"}})


@router.post("/token")
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
) -> Token:
    user = crud.get_user_by_username(username=form_data.username)
    user = authenticate_user(user, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.post("/register")
async def register(
        obj_in: UserCreate,
        email_code: EmailCode,
        r=Depends(get_redis),
) -> Res:
    email = obj_in.email
    if crud.get_user_by_email(email=email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    if crud.get_user_by_username(username=obj_in.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )
    if not r.get(email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Code expired",
        )
    print(r.get(email))
    if email_code.code != r.get(email).decode("utf-8"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Code error",
        )

    data: UserPublic = crud.create_user(obj_in=obj_in)
    r.delete(email)
    return Res(data=data.model_dump())


@router.post("/send_code")
async def send_code(
        email_code: EmailCode, background_tasks: BackgroundTasks, r=Depends(get_redis)
) -> Res:
    email = email_code.email
    background_tasks.add_task(generate_email, email, r)
    return Res(msg="Send success")


@router.patch("/reset_password")
async def reset_password(
        obj_in: UserCreate,
        email_code: EmailCode,
        r=Depends(get_redis),
) -> Res:
    email = obj_in.email
    if not crud.get_user_by_email(email=email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email not registered",
        )
    if not r.get(email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Code expired",
        )
    if email_code.code != r.get(email).decode("utf-8"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Code error",
        )

    data: UserPublic = crud.patch_user_by_email(obj_in=obj_in)
    r.delete(email)
    return Res(data=data.model_dump())
