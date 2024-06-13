from typing import Sequence

from fastapi import HTTPException
from sqlmodel import Session, select

from .models import User, UserCreate, UserUpdate, UserPublic
from .utils.auth import hash_password


class UserCRUD():
    def get_user(self, session: Session, offset=0, limit=10) -> Sequence[UserPublic]:
        users = session.exec(select(User).offset(offset).limit(limit)).all()
        return [UserPublic(**user.model_dump()) for user in users]

    def get_user_by_id(
            self,
            session: Session,
            pk: int,
    ) -> UserPublic:
        user: User | None = session.get(User, pk)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return UserPublic(**user.model_dump())

    def create_user(self, session: Session, obj_in: UserCreate) -> UserPublic:
        hashed_password = hash_password(obj_in.password)
        extra_data = {"hashed_password": hashed_password}
        user = User.model_validate(obj_in, update=extra_data)
        session.add(user)
        session.commit()
        session.refresh(user)
        return UserPublic(**user.model_dump())

    def patch_user(self, session: Session, pk: int, obj_in: UserUpdate) -> UserPublic:
        user: User | None = session.get(User, pk)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        user_data = obj_in.model_dump(exclude_unset=True)
        extra_data = {}
        if "password" in user_data:
            password = user_data["password"]
            hashed_password = hash_password(password)
            extra_data["hashed_password"] = hashed_password
        user.sqlmodel_update(user_data, update=extra_data)
        session.add(user)
        session.commit()
        session.refresh(user)
        return UserPublic(**user.model_dump())

    def delete_user(self, session: Session, pk: int):
        obj: User | None = session.get(User, pk)
        if not obj:
            raise HTTPException(status_code=404, detail="User not found")
        session.delete(obj)
        session.commit()
        return True
