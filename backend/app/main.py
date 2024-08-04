from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.app.config.db import init_db



@asynccontextmanager
async def lifespan():
    init_db()
    yield


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
