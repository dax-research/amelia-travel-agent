"""Business logic service for user authentication and authorization."""

from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi import HTTPException, status

from app.core.config import settings
from app.core.security import create_access_token, get_password_hash, verify_password
from app.schemas.auth import Token, UserLogin, UserRegister, UserResponse
from app.services.base import BaseService


class AuthService(BaseService):
    """Handles credentials verification, password hashing, and token issuance."""

    # In-memory mock store for development until database engine is connected
    _mock_users: dict = {}

    def register(self, payload: UserRegister) -> UserResponse:
        """Register a new traveler account."""
        if payload.email in self._mock_users:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email already exists.",
            )

        hashed = get_password_hash(payload.password)
        user_id = f"usr_{len(self._mock_users) + 1:04d}"
        user_record = {
            "id": user_id,
            "email": payload.email,
            "full_name": payload.full_name,
            "hashed_password": hashed,
            "is_active": True,
            "created_at": datetime.now(timezone.utc),
        }
        self._mock_users[payload.email] = user_record
        self.log_action("user_registered", {"user_id": user_id, "email": payload.email})

        return UserResponse(
            id=user_id,
            email=payload.email,
            full_name=payload.full_name,
            is_active=True,
            created_at=user_record["created_at"],
        )

    def login(self, payload: UserLogin) -> Token:
        """Authenticate user credentials and issue JWT."""
        user = self._mock_users.get(payload.email)
        if not user or not verify_password(payload.password, user["hashed_password"]):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password.",
                headers={"WWW-Authenticate": "Bearer"},
            )

        token_str = create_access_token(
            subject=user["id"],
            claims={"email": user["email"], "role": "traveler"},
            expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        )
        self.log_action("user_logged_in", {"user_id": user["id"]})

        return Token(
            access_token=token_str,
            token_type="bearer",
            expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        )


auth_service = AuthService()
