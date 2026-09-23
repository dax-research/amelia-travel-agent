"""Common FastAPI dependencies for authentication and request context."""

from typing import Any, Dict, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.core.config import settings
from app.core.security import decode_access_token

# OAuth2 password bearer scheme pointing to login route
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_PREFIX}/auth/login",
    auto_error=False,
)


def get_token_payload(token: Optional[str] = Depends(oauth2_scheme)) -> Dict[str, Any]:
    """Validate token and return payload. Raises 401 if missing or invalid."""
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication token required",
            headers={"WWW-Authenticate": "Bearer"},
        )
    try:
        payload = decode_access_token(token)
        if "sub" not in payload:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token payload missing subject identifier",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return payload
    except ValueError as err:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(err),
            headers={"WWW-Authenticate": "Bearer"},
        )


def get_current_user_id(payload: Dict[str, Any] = Depends(get_token_payload)) -> str:
    """Extract authenticated user id (sub claim) from token payload."""
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return str(user_id)
