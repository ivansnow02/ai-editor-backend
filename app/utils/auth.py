import os
from datetime import datetime, timedelta, timezone
from typing import Union

from jose import jwt
from passlib.context import CryptContext

from app.models import User
from config import settings

# openssl rand -hex 32
SECRET_KEY = os.getenv("SECRET_KEY")
# openssl rand -hex 10
SALT = os.getenv("SALT")

ALGORITHM = settings.AUTH.get("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = settings.AUTH.get("ACCESS_TOKEN_EXPIRE_MINUTES", 30)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_salt(password: str) -> str:
    """

    :param password: plain password
    :return: salted password
    """
    return f"{password}{SALT}"


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """

    :param plain_password:
    :param hashed_password:
    :return:
    """
    return pwd_context.verify(get_password_salt(plain_password), hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(get_password_salt(password))


def authenticate_user(user: User, password: str):
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
