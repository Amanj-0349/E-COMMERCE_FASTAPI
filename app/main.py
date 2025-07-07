from fastapi import FastAPI
from app import models
from app.database import engine
from app.routers import router  # routers.py imported here

models.Base.metadata.create_all(bind=engine)  # creates tables

app = FastAPI()

app.include_router(router)  # includes all endpoints defined in routers.py
