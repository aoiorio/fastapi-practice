# magic!!
from fastapi import FastAPI, Depends, HTTPException, Path, status
import models
from database import engine
from routers import auth, todos


app = FastAPI()

# create new database if the DB does not exit.(maybe same name???)
models.Base.metadata.create_all(bind=engine)

# you can use whatever you want if you write all of routers that you want to connect with same URL
app.include_router(auth.router)
app.include_router(todos.router)