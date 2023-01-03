import os
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "sounds-pathfinder"
    ENV = os.getenv('ENV')
    SQLALCHEMY_DATABASE_URL: str = os.getenv('SQLALCHEMY_DATABASE_URL')

    class Config:
        env_file = '.env'


settings = Settings()
