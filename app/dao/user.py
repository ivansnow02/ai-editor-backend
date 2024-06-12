

from . import BaseDAO
from app.models import UserModel
from app.models.schema import UserCreateSchema, UserSchema

class UserDAO(BaseDAO[UserModel, UserCreateSchema, UserCreateSchema]):
    model = UserModel