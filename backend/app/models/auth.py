from sqlmodel import Field
from backend.app.models.common import BaseModel


class User(BaseModel):
    email: str = Field(sa_column_kwargs={"unique": True})
    full_name: str
    hashed_password: str
    is_active: bool = True
    is_superuser: bool = False
