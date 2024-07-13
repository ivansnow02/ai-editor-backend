import redis
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

from config import settings
from . import crud
from .models import TokenData, UserPublic
from .utils.auth import ALGORITHM, SECRET_KEY

REDIS_HOST = settings.REDIS.HOST
REDIS_PORT = settings.REDIS.PORT
REDIS_DB = settings.REDIS.DB

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



def get_redis():
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
    try:
        yield r
    finally:
        r.close()


class CommonQueryParams:
    def __init__(self, offset: int = 1, limit: int = 10):
        self.offset = offset - 1
        if self.offset < 0:
            self.offset = 0
        self.limit = limit

        if self.limit < 0:
            self.limit = 10


def get_current_user(token: str = Depends(oauth2_scheme)) -> UserPublic:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="无法验证凭据",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except jwt.JWTError:
        raise credentials_exception
    user = crud.get_user_by_username(username=token_data.username)
    if user is None:
        raise credentials_exception
    return UserPublic(**user.model_dump())
