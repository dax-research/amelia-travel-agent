import datetime as dt
from typing import List, Optional
from pydantic import BaseModel, Field


class ItineraryItemBase(BaseModel):
    """Core attributes of a single itinerary activity/item."""

    time: Optional[str] = "09:00"
    title: str
    description: Optional[str] = None
    location: Optional[str] = None
    category: str = "activity"  # activity, dining, flight, hotel, transit, leisure
    estimated_duration_mins: Optional[int] = 60
    cost_estimate: Optional[float] = None
    booking_reference: Optional[str] = None


class ItineraryItemCreate(ItineraryItemBase):
    """Payload to insert a new activity into a day."""

    pass


class ItineraryItemUpdate(BaseModel):
    """Payload to update an existing activity item."""

    time: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    category: Optional[str] = None
    estimated_duration_mins: Optional[int] = None
    cost_estimate: Optional[float] = None


class ItineraryDayDetail(BaseModel):
    """Full day details containing a schedule of items."""

    day_number: int
    date: Optional[dt.date] = None
    theme: Optional[str] = None
    items: List[ItineraryItemBase] = Field(default_factory=list)


class ItineraryGenerateRequest(BaseModel):
    """Request payload to auto-generate a full itinerary using AI Concierge."""

    trip_id: str
    destination: str
    days: int = Field(default=3, ge=1, le=30)
    interests: List[str] = Field(default_factory=list)
    pace: str = "balanced"  # relaxed, balanced, intensive


class ItineraryResponse(BaseModel):
    """Full itinerary representation for a trip."""

    trip_id: str
    destination: str
    total_days: int
    days: List[ItineraryDayDetail] = Field(default_factory=list)
    generated_at: dt.datetime
