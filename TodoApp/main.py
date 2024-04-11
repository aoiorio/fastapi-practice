# magic!!
from fastapi import FastAPI
import models
from database import engine



app = FastAPI()

# create new database
models.Base.metadata.create_all(bind=engine)