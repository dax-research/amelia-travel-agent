"""Pydantic schemas for unified travel bookings (flights, hotels, activities)."""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field


class BookingType(str, Enum):
    """Supported booking categories."""

    FLIGHT = "flight"
    HOTEL = "hotel"
    ACTIVITY = "activity"


class BookingStatus(str, Enum):
    """Lifecycle states of a booking."""

    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
    MODIFIED = "modified"


class BookingCreate(BaseModel):
    """Payload to book a flight, hotel, or activity."""

    trip_id: Optional[str] = None
    booking_type: BookingType
    item_id: str  # flight_offer_id or hotel_offer_id
    total_amount: float = Field(..., gt=0)
    currency: str = "USD"
    details: Dict[str, Any] = Field(default_factory=dict)


class BookingResponse(BaseModel):
    """Representation of a completed booking record."""

    id: str
    user_id: str
    trip_id: Optional[str] = None
    booking_reference: str
    booking_type: BookingType
    status: BookingStatus
    total_amount: float
    currency: str
    details: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
