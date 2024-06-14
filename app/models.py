from sqlmodel import Field, SQLModel


class Token(SQLModel):
    access_token: str
    token_type: str


class TokenData(SQLModel):
    username: str | None = None


class UserBase(SQLModel):
    username: str = Field(index=True)
    email: str = Field(index=True)
    access: int = Field(default=0)
    avatar: str | None = Field(default=None)


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str = Field()

    # images: list["Image"] = Relationship(back_populates="user")


class UserCreate(UserBase):
    password: str


class UserUpdate(SQLModel):
    username: str | None = None
    email: str | None = None
    access: int | None = None
    avatar: str | None = None
    password: str | None = None


class UserPublic(UserBase):
    id: int


# class Image(SQLModel, table=True):

#     id: int | None = Field(default=None, primary_key=True)
#     path: str = Field(index=True)
#     despcription: str | None = Field(default=None)
#     owner_id: int = Field(foreign_key="users.id")
#     owner: User = Relationship(back_populates="images")
