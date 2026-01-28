from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError

from app.config.settings import settings


def create_access_token(user_id: int) -> str:
    now = datetime.now(timezone.utc)
    exp = now + timedelta(minutes=settings.access_token_minutes)

    payload = {
        "sub": str(user_id),  # subject, who the token belongs to
        "iat": int(now.timestamp()),  # issued at
        "exp": int(exp.timestamp()),  # expiry
    }
    return jwt.encode(payload, settings.jwt_secret, algorithm=settings.jwt_algorithm)


def decode_access_token(token: str) -> int:
    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])
    except JWTError as e:
        raise ValueError("Invalid token") from e

    sub = payload.get("sub")
    if sub is None:
        raise ValueError("Invalid token")

    try:
        return int(sub)
    except ValueError as e:
        raise ValueError("Invalid token") from e
