import sys

sys.path.append("..")

from typing import Optional
from fastapi import Depends, APIRouter, Request, Form
from ..models import *
from ..database import engine, SessionLocal
from sqlalchemy.orm import Session
from .auth import get_current_user, get_password_hash, verify_password
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from starlette import status
from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# . means that go back to src
templates = Jinja2Templates(directory="./TodoAppFullStack/templates")

# print(Path(BASE_DIR, 'templates'))

router = APIRouter(
    prefix="/users", tags=["users"], responses={404: {"description": "Not found"}}
)

Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

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

    user_model = db.query(Users).filter(Users.id == user.get("id")).first()
    response = RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)

    # validation password that input and current password in the database
    validation_password = verify_password(current_password, user_model.hashed_password)

    if not validation_password or user_model.username != username:
        msg = "Incorrect Username or Password"
        return templates.TemplateResponse("change-password.html", {"request": request, "user": user, "msg": msg})

    new_hashed_password = get_password_hash(new_password)
    user_model.hashed_password = new_hashed_password

    db.add(user_model)
    db.commit()

    return response
