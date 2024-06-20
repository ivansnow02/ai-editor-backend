from typing import Sequence

from fastapi import HTTPException
from sqlmodel import Session, select

from .models import ImageModel, ImagePublic, User, UserCreate, UserPublic, UserUpdate
from .utils.auth import get_password_hash


def get_user(session: Session, offset=0, limit=10) -> Sequence[UserPublic]:
    users = session.exec(select(User).offset(offset).limit(limit)).all()
    return [UserPublic(**user.model_dump()) for user in users]


def get_user_by_id(
    session: Session,
    pk: int,
) -> UserPublic:
    user: User | None = session.get(User, pk)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserPublic(**user.model_dump())


def create_user(session: Session, obj_in: UserCreate) -> UserPublic:
    hashed_password = get_password_hash(obj_in.password)
    extra_data = {"hashed_password": hashed_password}
    user = User.model_validate(obj_in, update=extra_data)
    session.add(user)
    session.commit()
    session.refresh(user)
    return UserPublic(**user.model_dump())


def patch_user(session: Session, pk: int, obj_in: UserUpdate) -> UserPublic:
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


def delete_user(session: Session, pk: int):
    obj: User | None = session.get(User, pk)
    if not obj:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(obj)
    session.commit()
    return True


def get_user_by_username(session: Session, username: str) -> User | None:
    user = session.query(User).filter(User.username == username).first()
    return user


def get_user_by_email(session: Session, email: str) -> User | None:
    user = session.query(User).filter(User.email == email).first()
    return user


def create_img(session: Session, img: ImageModel) -> ImagePublic:
    session.add(img)
    session.commit()
    session.refresh(img)
    url = "/api/img/" + str(img.id)
    img_public = ImagePublic(id=img.id, url=url)
    return img_public


def get_img(session: Session, pk: int) -> ImageModel:
    img: ImageModel | None = session.get(ImageModel, pk)
    if not img:
        raise HTTPException(status_code=404, detail="Image not found")
    return img
