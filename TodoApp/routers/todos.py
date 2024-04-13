# magic!!
from models import Todos
from database import SessionLocal
from typing import Annotated
import models
from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field

router = APIRouter()

def get_db():
    db = SessionLocal()
    # close db after return db
    try:
        # YIELD means that return something, except the function will return a generator.
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


# Male validation
class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool


# return all the data
@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(models.Todos).all()


@router.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    # if the todo not found, we'll return the status_code of 404.
    raise HTTPException(status_code=404, detail="Todo not found.")


# create todo by using db
@router.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todo_request: TodoRequest):
    todo_model = Todos(**todo_request.dict())

    # add means adding a data to the db.
    db.add(todo_model)

    # commit the data you added
    db.commit()


@router.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(
    db: db_dependency, todo_request: TodoRequest, todo_id: int = Path(gt=0)
):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found.")

    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit()


@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()

    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo _not found.")

    db.query(Todos).filter(Todos.id == todo_id).delete()

    db.commit()
