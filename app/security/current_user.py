from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.security.jwt import decode_access_token

bearer_scheme = HTTPBearer()


def get_current_user_id(
    creds: HTTPAuthorizationCredentials = Security(bearer_scheme),
) -> int:
    token = creds.credentials
    try:
        return decode_access_token(token)
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
