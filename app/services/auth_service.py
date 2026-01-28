from sqlalchemy.orm import Session

from app.repositories.users_sql_repo import UsersSqlRepository
from app.schemas.users import UserOut
from app.security.passwords import hash_password
from app.security.passwords import verify_password
from app.security.jwt import create_access_token


class AuthService:
    def __init__(self, db: Session):
        self._users = UsersSqlRepository(db)

    def register(self, email: str, password: str) -> UserOut:
        existing = self._users.get_by_email(email)
        if existing is not None:
            raise ValueError("Email already registered")

        row = self._users.create(email=email, password_hash=hash_password(password))
        return UserOut(id=row.id, email=row.email)

    def login(self, email: str, password: str) -> str:
        user = self._users.get_by_email(email)
        if user is None:
            raise ValueError("Invalid credentials")

        if not verify_password(password, user.password_hash):
            raise ValueError("Invalid credentials")

        return create_access_token(user_id=user.id)
