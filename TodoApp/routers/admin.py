# magic!!
from ..models import Todos
from ..database import SessionLocal

from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from .auth import get_current_user

# Clean the order by using tags and prefix
router = APIRouter(
    prefix='/admin',
    tags=['admin']
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


@router.get('/todo', status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):
    if user is None or user.get('user_role') != "admin":
        raise HTTPException(status_code=401, detail='Authentication Failed 😩')
    return db.query(Todos).all()

@router.delete('/todo/{todo_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=401, detail='Authentication Failed 😩')

    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()

    # Check the value is None
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found. 😩')

    db.query(Todos).filter(Todos.id == todo_id).delete()

    db.commit()