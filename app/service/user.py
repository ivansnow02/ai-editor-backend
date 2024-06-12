from ..dao.user import UserDAO
from app.models import UserModel, UserCreateSchema, UserSchema
from . import BaseService

class UserService(BaseService[UserModel, UserCreateSchema, UserCreateSchema]):
    dao = UserDAO()
    model = UserModel
    create_schema = UserCreateSchema
    update_schema = UserCreateSchema
    schema = UserSchema