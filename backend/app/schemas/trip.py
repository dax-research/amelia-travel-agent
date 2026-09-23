import datetime as dt
from typing import List, Optional
from pydantic import BaseModel, Field


class ItineraryItem(BaseModel):
    """Single activity or stop within an itinerary."""

    time: Optional[str] = None
    title: str
    description: Optional[str] = None
    location: Optional[str] = None
    category: Optional[str] = "activity"  # activity, dining, flight, hotel, transit
    cost_estimate: Optional[float] = None


class ItineraryDay(BaseModel):
    """Daily schedule within a trip itinerary."""

    day_number: int
    date: Optional[dt.date] = None
    theme: Optional[str] = None
    items: List[ItineraryItem] = Field(default_factory=list)


class TripBase(BaseModel):
    """Base trip properties."""

    destination: str
    origin: Optional[str] = None
    start_date: dt.date
    end_date: dt.date
    budget: Optional[float] = None
    travelers_count: int = Field(default=1, ge=1)
    preferences: List[str] = Field(default_factory=list)


class TripCreate(TripBase):
    """Payload for creating a new trip."""

    pass


class TripUpdate(BaseModel):
    """Payload for updating an existing trip."""

    destination: Optional[str] = None
    start_date: Optional[dt.date] = None
    end_date: Optional[dt.date] = None
    budget: Optional[float] = None
    travelers_count: Optional[int] = None
    preferences: Optional[List[str]] = None


class TripResponse(TripBase):
    """Trip detail response including ID and itinerary days."""

    id: str
    user_id: str
    status: str = "planned"  # planned, active, completed, cancelled
    itinerary: List[ItineraryDay] = Field(default_factory=list)
    created_at: dt.datetime
    updated_at: dt.datetime

    model_config = {"from_attributes": True}
