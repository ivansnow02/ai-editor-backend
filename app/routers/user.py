from typing import Sequence

from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.crud import UserCRUD
from app.dependencies import get_db
from ..models import UserCreate, UserPublic, UserUpdate
from ..utils.result import Res

router = APIRouter(
    prefix='/api/user',
    tags=['user'],
    responses={404: {'description': 'Not found'}}
)

_user_crud = UserCRUD()


@router.get("/{pk}", response_model=Res)
def get_user_by_id(pk: int, session: Session = Depends(dependency=get_db)) -> Res:
    data: UserPublic = _user_crud.get_user_by_id(session=session, pk=pk)
    return Res(data=data.model_dump())


@router.post(path='/', response_model=Res)
def create_user(
        obj_in: UserCreate,
        session: Session = Depends(dependency=get_db)
) -> Res:
    data: UserPublic = _user_crud.create_user(session=session, obj_in=obj_in)

    return Res(data=data.model_dump())


@router.get(path="/", response_model=Res)
def get_user(
        session: Session = Depends(dependency=get_db)
) -> Res:
    data: Sequence[UserPublic] = _user_crud.get_user(session=session)
    return Res(data=[i.model_dump() for i in data])


@router.patch(path="/{pk}", response_model=Res)
def patch_user(
        pk: int,
        obj_in: UserUpdate,
        session: Session = Depends(dependency=get_db)
) -> Res:
    data: UserPublic = _user_crud.patch_user(session=session, pk=pk, obj_in=obj_in)
    return Res(data=data.model_dump())


@router.delete(path="/{pk}", response_model=Res)
def delete_user(
        pk: int,
        session: Session = Depends(dependency=get_db)
) -> Res:
    _user_crud.delete_user(session=session, pk=pk)
    return Res()
