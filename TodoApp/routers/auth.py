from fastapi import APIRouter, Depends, status, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from passlib.context import CryptContext
from database import SessionLocal
from typing import Annotated

from models import Users

router = APIRouter()


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str


def get_db():
    db = SessionLocal()
    # close db after return db
    try:
        # YIELD means that return something, except the function will return a generator.
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/auth/", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        # Hash the password by using bcrypt and passlib packages.
        hashed_password=bcrypt_context.hash(create_user_request.password),
        role=create_user_request.role,
        is_active=True,
    )

    db.add(create_user_model)
    db.commit()


@router.get("/get_user/{user_id}", status_code=status.HTTP_200_OK)
async def get_user_from_id(db: db_dependency, user_id: int):
    user_model = db.query(Users).filter(Users.id == user_id).first()

    if user_model is None:
        raise HTTPException(status_code=404, detail="The user not found.")

    return user_model


@router.get("/users", status_code=status.HTTP_200_OK)
async def get_user(db: db_dependency):
    users = db.query(Users).all()
    return users
