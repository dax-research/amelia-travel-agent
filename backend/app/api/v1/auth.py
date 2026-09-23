"""Authentication API endpoints."""

from fastapi import APIRouter, status
from app.schemas.auth import Token, UserLogin, UserRegister, UserResponse
from app.schemas.common import ApiResponse
from app.services.auth_service import auth_service

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post(
    "/register",
    response_model=ApiResponse[UserResponse],
    status_code=status.HTTP_201_CREATED,
    summary="Register a new traveler account",
)
async def register(payload: UserRegister) -> ApiResponse[UserResponse]:
    """Register a new user account with email and password."""
    user = auth_service.register(payload)
    return ApiResponse(
        success=True,
        message="Account created successfully.",
        data=user,
    )


@router.post(
    "/login",
    response_model=Token,
    summary="Login to obtain JWT access token",
)
async def login(payload: UserLogin) -> Token:
    """Authenticate and return JWT bearer token."""
    return auth_service.login(payload)
