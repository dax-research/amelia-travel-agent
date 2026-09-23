"""Business logic for user profile and preference management."""

from datetime import datetime, timezone
from typing import Dict, Optional
from fastapi import HTTPException, status

from app.schemas.user import TravelPreferences, UserProfile, UserProfileUpdate
from app.services.base import BaseService
from app.utils.helpers import utc_now


class UserService(BaseService):
    """Manages user profile data and travel preferences."""

    _profiles: Dict[str, dict] = {}

    def get_profile(self, user_id: str) -> UserProfile:
        """Retrieve user profile or initialize default traveler profile."""
        if user_id not in self._profiles:
            now = utc_now()
            self._profiles[user_id] = {
                "id": user_id,
                "email": f"{user_id}@traveler.example.com",
                "full_name": "Traveler",
                "phone_number": "+1 (555) 019-2834",
                "preferences": TravelPreferences().model_dump(),
                "created_at": now,
                "updated_at": now,
            }
        data = self._profiles[user_id]
        return UserProfile(**data)

    def update_profile(self, user_id: str, payload: UserProfileUpdate) -> UserProfile:
        """Update profile fields and travel personalization preferences."""
        profile = self.get_profile(user_id)
        data = profile.model_dump()

        if payload.full_name is not None:
            data["full_name"] = payload.full_name
        if payload.phone_number is not None:
            data["phone_number"] = payload.phone_number
        if payload.preferences is not None:
            data["preferences"] = payload.preferences.model_dump()

        data["updated_at"] = utc_now()
        self._profiles[user_id] = data
        self.log_action("profile_updated", {"user_id": user_id})
        return UserProfile(**data)


user_service = UserService()
