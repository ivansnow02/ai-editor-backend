from pydantic import BaseModel



class ImageBaseSchema(BaseModel):
    path: str
    description: str | None = None


class ImageCreateSchema(ImageBaseSchema):
    pass


class ImageSchema(ImageBaseSchema):
    id: int
    owner_id: int
    class Config:
        orm_mode = True


class UserBaseSchema(BaseModel):
    email: str
    username: str


class UserCreateSchema(UserBaseSchema):
    
    password: str

class UserUpdateSchema(UserBaseSchema):
    password: str
    username: str
    email: str

class UserSchema(UserBaseSchema):
    id: int
    access: int = 0
    username: str
    avatar: str | None = None
    images: list[ImageSchema] = []

    class Config:
        orm_mode = True
