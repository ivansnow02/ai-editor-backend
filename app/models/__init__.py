from typing import TypeVar

from pydantic import BaseModel

from ..db import Base
from .user import UserModel
from .img import ImageModel
from .schema import UserCreateSchema, UserSchema, ImageCreateSchema, ImageSchema


__all__ = [ "UserModel", "ImageModel", "UserCreateSchema", "UserSchema", "ImageCreateSchema", "ImageSchema" ]

CreateSchema = TypeVar("CreateSchema", bound=BaseModel)
UpdateSchema = TypeVar("UpdateSchema", bound=BaseModel)
ModelType = TypeVar("ModelType", bound=Base)
