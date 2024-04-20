# magic!!
from fastapi import FastAPI, Depends, HTTPException, Path, status
from .models import Base
from .database import engine
from .routers import auth, todos, admin, users


app = FastAPI()

# create new database if the DB does not exit.(maybe same name???)
Base.metadata.create_all(bind=engine)

@app.get('/healthy')
def heal_check():
    return {'status': 'Healthy'}

# you can use whatever you want if you write all of routers that you want to connect with same URL
app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)