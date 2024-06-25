from typing import Sequence

from fastapi import HTTPException
from sqlmodel import Session, select

from .db import engine
from .models import ImageModel, ImagePublic, User, UserCreate, UserPublic, UserUpdate
from .utils.auth import get_password_hash


def get_user(offset=0, limit=10) -> Sequence[UserPublic]:
    with Session(engine) as session:
        users = session.exec(select(User).offset(offset).limit(limit)).all()
        return [UserPublic(**user.model_dump()) for user in users]


def get_user_by_id(
    pk: int,
) -> UserPublic:
    with Session(engine) as session:
        user: User | None = session.get(User, pk)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return UserPublic(**user.model_dump())


def create_user(obj_in: UserCreate) -> UserPublic:
    hashed_password = get_password_hash(obj_in.password)
    extra_data = {"hashed_password": hashed_password}
    user = User.model_validate(obj_in, update=extra_data)
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return UserPublic(**user.model_dump())


def patch_user(pk: int, obj_in: UserUpdate) -> UserPublic:
    with Session(engine) as session:
        user: User | None = session.get(User, pk)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        user_data = obj_in.model_dump(exclude_unset=True)
        extra_data = {}
        if "password" in user_data:
            password = user_data["password"]
            hashed_password = get_password_hash(password)
            extra_data["hashed_password"] = hashed_password
        user.sqlmodel_update(user_data, update=extra_data)
        session.add(user)
        session.commit()
        session.refresh(user)
        return UserPublic(**user.model_dump())


def delete_user(pk: int):
    with Session(engine) as session:
        obj: User | None = session.get(User, pk)
        if not obj:
            raise HTTPException(status_code=404, detail="User not found")
        session.delete(obj)
        session.commit()
        return True


def get_user_by_username(username: str) -> User | None:
    with Session(engine) as session:
        user = session.exec(select(User).where(User.username == username)).first()
        return user


def get_user_by_email(email: str) -> User | None:
    with Session(engine) as session:
        user = session.exec(select(User).where(User.email == email)).first()
        return user


def create_img(img: ImageModel) -> ImagePublic:
    with Session(engine) as session:
        session.add(img)
        session.commit()
        session.refresh(img)
        img_public = ImagePublic(id=img.id, url=img.path)
        return img_public


def get_img_user_id(path: str) -> int:
    with Session(engine) as session:
        img = session.exec(select(ImageModel).where(ImageModel.path == path)).first()
        return img.user_id
