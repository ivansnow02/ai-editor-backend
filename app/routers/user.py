from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.dependencies import get_current_user, get_db
from .. import crud
from ..models import UserCreate, UserPublic, UserUpdate
from ..utils.result import Res

router = APIRouter(
    prefix="/api/user", tags=["user"], responses={404: {"description": "Not found"}}
)


# @router.get("/{pk}", response_model=Res)
# def get_user_by_id(pk: int, session: Session = Depends(dependency=get_db)) -> Res:
#     data: UserPublic = crud.get_user_by_id(session=session, pk=pk)
#     return Res(data=data.model_dump())
#


@router.post(path="/", response_model=Res)
def create_user(
    obj_in: UserCreate, session: Session = Depends(dependency=get_db)
) -> Res:
    data: UserPublic = crud.create_user(session=session, obj_in=obj_in)

    return Res(data=data.model_dump())


# @router.get(path="/", response_model=Res)
# def get_user(session: Session = Depends(dependency=get_db)) -> Res:
#     data: Sequence[UserPublic] = crud.get_user(session=session)
#     return Res(data=[i.model_dump() for i in data])


@router.patch(path="/me", response_model=Res)
def patch_user(
    obj_in: UserUpdate,
    session: Session = Depends(dependency=get_db),
    current_user: UserPublic = Depends(get_current_user),
) -> Res:
    current_user_id = current_user.id
    data: UserPublic = crud.patch_user(
        session=session, pk=current_user_id, obj_in=obj_in
    )
    return Res(data=data.model_dump())


@router.delete(path="/me", response_model=Res)
def delete_user(
    current_user: UserPublic = Depends(get_current_user),
    session: Session = Depends(dependency=get_db),
) -> Res:
    current_user_id = current_user.id
    crud.delete_user(session=session, pk=current_user_id)
    return Res()


@router.get("/me", response_model=Res)
def read_users_me(current_user: UserPublic = Depends(get_current_user)):
    return Res(data=current_user.model_dump())
