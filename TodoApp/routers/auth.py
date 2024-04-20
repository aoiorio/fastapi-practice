from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, status, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from passlib.context import CryptContext
from ..database import SessionLocal
from typing import Annotated
# bearer means 使い.
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError

from ..models import Users

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

# Prepare for use jwt
SECRET_KEY = "85e7e91bc37ca9041e4ab9c15d37d91990bf3353df2c5d08cc06cfb587fac09d"
ALGORITHM = "HS256"


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')


class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str
    phone_number: str


class Token(BaseModel):
    access_token: str
    token_type: str



def get_db():
    db = SessionLocal()
    # close db after return db
    try:
        # YIELD means that return something, except the function will return a generator.
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

# Check the user can authenticate with the username and the password
def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user


def create_access_token(username: str, user_id: int, role: str,expires_delta: timedelta):
    encode = {"sub": username, "id": user_id, "role": role}

    expires = datetime.utcnow() + expires_delta
    encode.update({"exp": expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username: str = payload.get('sub') # sub is our username
        user_id: int = payload.get('id')
        user_role: str = payload.get('role')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user.')
        return {'username': username, 'id': user_id, 'user_role': user_role}

    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user.')




@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        # Hash the password by using bcrypt and passlib packages.
        hashed_password=bcrypt_context.hash(create_user_request.password),
        role=create_user_request.role,
        phone_number=create_user_request.phone_number,
        is_active=True,
    )

    db.add(create_user_model)
    db.commit()


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user.')


    token = create_access_token(user.username, user.id, user.role, timedelta(minutes=20))
    return {'access_token': token, 'token_type': 'bearer'}


# ----------- get user data that is in todosapp.db ----------
# @router.get("/get_user/{user_id}", status_code=status.HTTP_200_OK)
# async def get_user_from_id(db: db_dependency, user_id: int):
#     user_model = db.query(Users).filter(Users.id == user_id).first()

#     if user_model is None:
#         raise HTTPException(status_code=404, detail="The user not found.")

#     return user_model


# @router.get("/users", status_code=status.HTTP_200_OK)
# async def get_user(db: db_dependency):
#     users = db.query(Users).all()
#     return users

