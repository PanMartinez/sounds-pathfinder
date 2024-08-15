from fastapi import FastAPI
from soundfinder.config.db import engine, SessionLocal
from soundfinder.config.settings import Settings
from soundfinder.models.common import Base

Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_settings():
    return Settings()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
