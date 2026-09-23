"""User profile and travel preferences endpoints."""

from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_user_id
from app.schemas.common import ApiResponse
from app.schemas.user import UserProfile, UserProfileUpdate
from app.services.user_service import user_service

router = APIRouter(prefix="/users", tags=["Users"])


@router.get(
    "/me",
    response_model=ApiResponse[UserProfile],
    summary="Get current traveler profile and preferences",
)
async def get_my_profile(
    user_id: str = Depends(get_current_user_id),
) -> ApiResponse[UserProfile]:
    """Retrieve personal profile, loyalty preferences, and guardian notification settings."""
    profile = user_service.get_profile(user_id)
    return ApiResponse(
        success=True,
        message="Profile retrieved successfully.",
        data=profile,
    )


@router.patch(
    "/me",
    response_model=ApiResponse[UserProfile],
    summary="Update travel preferences and contact details",
)
async def update_my_profile(
    payload: UserProfileUpdate,
    user_id: str = Depends(get_current_user_id),
) -> ApiResponse[UserProfile]:
    """Update traveler preferences (dietary, seat choice, budget level, notification channels)."""
    updated = user_service.update_profile(user_id, payload)
    return ApiResponse(
        success=True,
        message="Profile updated successfully.",
        data=updated,
    )
