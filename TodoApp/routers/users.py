# magic!!
from database import SessionLocal
from typing import Annotated
import models
from models import Users
from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session
from .auth import get_current_user
from passlib.context import CryptContext
from pydantic import BaseModel, Field


# Clean the order by using tags and prefix
router = APIRouter(
    prefix='/user',
    tags=['user']
)

def get_db():
    db = SessionLocal()
    # close db after return db
    try:
        # YIELD means that return something, except the function will return a generator.
        yield db
    finally:
        db.close()


# Annotated means making clear the type of value
db_dependency = Annotated[Session, Depends(get_db)]

# Annotated means making clear the type of value
user_dependency = Annotated[dict, Depends(get_current_user)]

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=6)



@router.get('/')
async def get_users(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed 😩")

    user_id = user.get('id')
    user_model = db.query(Users).filter(Users.id == user_id).first()

    if user_model is None:
        raise HTTPException(status_code=401, detail="User not found")

    return user_model


@router.put('/password', status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user: user_dependency, db: db_dependency, user_verification: UserVerification):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed 😩")

    user_id = user.get('id')
    user_model = db.query(Users).filter(Users.id == user_id).first()

    if not bcrypt_context.verify(user_verification.password, user_model.hashed_password):
        raise HTTPException(status_code=401, detail="Error on password change 😩")

    user_model.hashed_password = bcrypt_context.hash(user_verification.new_password)

    db.add(user_model)
    db.commit()

# My answer!! Security is really weak, because it's not confirming the current password first.
"""
@router.put('/password/{new_password}', status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user: user_dependency, db: db_dependency, new_password: str):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed 😩")

    user_id = user.get('id')
    user_model = db.query(Users).filter(Users.id == user_id).first()

    new_hashed_password = bcrypt_context.hash(new_password)
    user_model.hashed_password = new_hashed_password

    db.add(user_model)
    db.commit()
"""

