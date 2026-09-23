"""Pydantic schemas for hotel searches and room reservations."""

from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field


class HotelSearchQuery(BaseModel):
    """Query parameters for hotel lodging search."""

    city: str
    check_in: date
    check_out: date
    guests: int = Field(default=1, ge=1)
    rooms: int = Field(default=1, ge=1)
    min_rating: Optional[float] = None
    max_price_per_night: Optional[float] = None


class HotelRoom(BaseModel):
    """Room option within a hotel offer."""

    room_type: str
    capacity: int
    bed_type: str
    price_per_night: float
    refundable: bool = True


class HotelOffer(BaseModel):
    """Hotel offer with details and room tiers."""

    id: str
    name: str
    city: str
    address: Optional[str] = None
    star_rating: float
    review_score: float
    price_per_night: float
    currency: str = "USD"
    amenities: List[str] = Field(default_factory=list)
    rooms: List[HotelRoom] = Field(default_factory=list)
