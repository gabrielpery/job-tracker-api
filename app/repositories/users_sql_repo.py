from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.infrastructure.db.models.user import UserModel


class UsersSqlRepository:
    def __init__(self, db: Session):
        self._db = db

    def get_by_email(self, email: str) -> Optional[UserModel]:
        return self._db.scalar(select(UserModel).where(UserModel.email == email))

    def create(self, email: str, password_hash: str) -> UserModel:
        row = UserModel(email=email, password_hash=password_hash)
        self._db.add(row)
        self._db.commit()
        self._db.refresh(row)
        return row
