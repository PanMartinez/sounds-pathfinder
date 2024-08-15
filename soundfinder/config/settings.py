import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ALGORITHM: str = os.getenv("ALGORITHM")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET")
    DATABASE_URL: str = os.getenv("DATABASE_URL")


settings = Settings()
