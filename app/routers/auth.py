from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from app import crud
from app.dependencies import get_db, get_redis
from app.models import Token, UserCreate, UserPublic
from app.utils import send_email
from app.utils.auth import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    authenticate_user,
    create_access_token,
)
from app.utils.result import Res

router = APIRouter(tags=["auth"], responses={404: {"description": "Not found"}})


@router.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(dependency=get_db),
) -> Token:
    user = crud.get_user_by_username(session=session, username=form_data.username)
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
    session: Session = Depends(dependency=get_db),
    code: str = None,
    r=Depends(get_redis),
) -> Res:
    email = obj_in.email
    if crud.get_user_by_email(session=session, email=email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    if crud.get_user_by_username(session=session, username=obj_in.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )
    if not r.get(email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Code expired",
        )
    if code != r.get(email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Code error",
        )

    data: UserPublic = crud.create_user(session=session, obj_in=obj_in)
    r.delete(email)
    return Res(data=data.model_dump())


@router.post("/send_code")
async def send_code(
    email: str, r=Depends(get_redis), session: Session = Depends(get_db)
) -> Res:
    email = email.strip()
    if crud.get_user_by_email(email=email, session=session):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    code = send_email.generate_email(email)
    r.set(email, code, ex=300)
    return Res(msg="Send success")
