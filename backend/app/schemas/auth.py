"""Pydantic schemas for authentication and authorization."""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    """Base user fields."""

    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool = True


class UserRegister(UserBase):
    """Payload for user registration."""

    password: str = Field(min_length=8, description="User password (min 8 characters)")


class UserLogin(BaseModel):
    """Payload for user login."""

    email: EmailStr
    password: str


class UserResponse(UserBase):
    """User response model returned to clients."""

    id: str
    created_at: datetime

    model_config = {"from_attributes": True}


class Token(BaseModel):
    """Bearer token response."""

    access_token: str
    token_type: str = "bearer"
    expires_in: int


class TokenPayload(BaseModel):
    """Decoded JWT claims."""

    sub: str
    role: Optional[str] = "traveler"
    email: Optional[str] = None
    exp: Optional[int] = None
