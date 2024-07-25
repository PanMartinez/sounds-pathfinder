import os
from functools import lru_cache
from pydantic import BaseSettings


@lru_cache()
def get_settings():
    return Settings()


class Settings(BaseSettings):

    # general settings
    APP_NAME: str = 'sounds-pathfinder'
    VERSION: str
    ENV: str

    # database settings
    SQLALCHEMY_DATABASE_URL: str

    # uvicorn settings
    # WORKERS_COUNT: int
    # HOST: str
    # PORT: int
    # RELOAD: bool

    class Config:
        env_file = '.env'
