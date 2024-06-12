from sqlalchemy.orm import Session
from app.models.user import UserModel
from ..utils.result import Res
from dependencies import get_db
from fastapi import APIRouter, Depends

from app.service.user import UserService

router = APIRouter(
    prefix='/api/user',
    tags=['user'],
    responses={404: {'description': 'Not found'}}
)
_service = UserService()

@router.get('/{pk}')
async def get_user(
    pk: int,
    session: Session = Depends(dependency=get_db)
    ) -> Res:
    data: UserModel | None = _service.get_by_id(session=session, pk=pk)
    if data is None:
        return Res(code=404, msg='User not found')
    return Res(data=data)

# TODO: Add more routes for user