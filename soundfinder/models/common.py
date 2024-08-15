from datetime import datetime
from uuid import uuid4
from typing import Optional
from sqlalchemy import Column, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id: UUID = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    created_at: datetime = Column(DateTime(), default=func.now())
    updated_at: Optional[datetime] = Column(DateTime(), onupdate=func.now())
