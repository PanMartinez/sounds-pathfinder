from datetime import datetime
from uuid import UUID, uuid4
from typing import Optional
from sqlalchemy import Column, DateTime, func
from sqlmodel import Field, SQLModel


class BaseModel(SQLModel):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(
        sa_column=Column(DateTime(), onupdate=func.now())
    )
