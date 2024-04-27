import sys

sys.path.append("..")

from typing import Optional
from fastapi import Depends, APIRouter, Request, Form
from ..models import *
from ..database import engine, SessionLocal
from .auth import get_current_user, get_password_hash, verify_password
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from starlette import status
from passlib.context import CryptContext

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter(
    prefix="/users", tags=["users"], responses={404: {"description": "Not found"}}
)

Base.metadata.create_all(bind=engine)

# . means that go back to src
templates = Jinja2Templates(directory="./TodoAppFullStack/templates")

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class UserVerification(BaseModel):
    username: str
    password: str
    new_password: str


@router.get("/", response_class=HTMLResponse)
async def get_user(request: Request, db: Session = Depends(get_db)):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)
    user_model = db.query(Users).filter(Users.id == user.get("id")).first()

    username = user_model.username
    user_password = user_model.hashed_password

    return templates.TemplateResponse("verify-user.html", {"request": request, "username": username, "user_password": user_password, "user": user})



@router.get("/change-password", response_class=HTMLResponse)
async def change_password(request: Request):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    return templates.TemplateResponse("change-password.html", {"request": request, "user": user})

@router.post("/change-password", response_class=HTMLResponse)
async def change_password_submit(request: Request, username: str = Form(...), current_password: str = Form(...), new_password: str = Form(...), db: Session = Depends(get_db)):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    user_data = db.query(Users).filter(Users.id == user.get("id")).first()
    msg = "Incorrect Username or Password"

    # validation password that input and current password in the database
    validation_password = verify_password(current_password, user_data.hashed_password)

    # Simple is power!
    if user_data is not None:

        if validation_password and user_data.username == username:
            new_hashed_password = get_password_hash(new_password)
            user_data.hashed_password = new_hashed_password

            db.add(user_data)
            db.commit()

            msg = "Password Updated"

        # if the user tried to change to same password
        if current_password == new_password:
            msg = "This new password is already used. Please try another password."

    return templates.TemplateResponse("change-password.html", {"request": request, "user": user, "msg": msg})
