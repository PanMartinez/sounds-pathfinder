from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer
from jwt import encode, decode
from soundfinder.config.settings import settings
from soundfinder.models.auth import User


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# ----- JWT Token -----
async def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    return encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


async def decode_token(token: str):
    return decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])


# ----- User Authentication -----
async def get_user(email: str):
    return User(email=email)
