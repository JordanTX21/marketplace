from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from tortoise.exceptions import DoesNotExist

from src.config.db import SessionLocal
from src.models.user import users
from src.schemas.user import User


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

conn = SessionLocal()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


async def get_user(username: str):
    data = conn.execute(users.select().where(users.c.name == username)).first()
    user = dict(data._mapping)
    return await User.from_queryset_single(user)


async def validate_user(user: OAuth2PasswordRequestForm = Depends()):
    try:
        data = conn.execute(users.select().where(users.c.name == user.username)).first()
        db_user = dict(data._mapping)
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    if not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    return db_user