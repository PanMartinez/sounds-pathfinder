from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import UUID
from soundfinder.models.auth import User
from soundfinder.schemas.auth import UserCreateSchema


def get_all_users(db: Session) -> list[User] | None:
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: UUID) -> User | None:
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user_data: UserCreateSchema) -> User:
    user = User(
        email=user_data.email,
        hashed_password=user_data.password,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user
