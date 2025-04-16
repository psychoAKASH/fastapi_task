from fastapi import FastAPI
from app.api.routes import router
from app.db.database import engine
from app.models import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(router)
