"""Pydantic schemas for user profile and travel preferences."""

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field


class TravelPreferences(BaseModel):
    """Traveler personalization preferences."""

    preferred_airline: Optional[str] = None
    seat_preference: Optional[str] = "window"  # window, aisle, middle
    dietary_restrictions: List[str] = Field(default_factory=list)
    budget_tier: Optional[str] = "moderate"  # budget, moderate, luxury
    hotel_amenities: List[str] = Field(default_factory=list)
    auto_rebook_on_disruption: bool = True
    push_notifications: bool = True
    sms_notifications: bool = False


class UserProfile(BaseModel):
    """User profile response representation."""

    id: str
    email: EmailStr
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    preferences: TravelPreferences = Field(default_factory=TravelPreferences)
    created_at: datetime
    updated_at: datetime


class UserProfileUpdate(BaseModel):
    """Payload for updating user profile information."""

    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    preferences: Optional[TravelPreferences] = None
