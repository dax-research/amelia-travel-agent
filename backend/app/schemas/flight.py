"""Pydantic schemas for flight search, tracking, and bookings."""

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class FlightSearchQuery(BaseModel):
    """Parameters for flight availability queries."""

    origin: str = Field(..., min_length=3, max_length=4, description="IATA airport code, e.g. JFK")
    destination: str = Field(..., min_length=3, max_length=4, description="IATA airport code, e.g. LHR")
    departure_date: str = Field(..., description="Date formatted as YYYY-MM-DD")
    return_date: Optional[str] = None
    passengers: int = Field(default=1, ge=1, le=9)
    cabin_class: str = "economy"  # economy, premium_economy, business, first


class FlightSegment(BaseModel):
    """Single flight leg in an itinerary."""

    flight_number: str
    airline: str
    airline_code: str
    departure_airport: str
    arrival_airport: str
    departure_time: datetime
    arrival_time: datetime
    duration_mins: int


class FlightOffer(BaseModel):
    """Flight offer response with pricing and segments."""

    id: str
    airline: str
    origin: str
    destination: str
    departure_time: datetime
    arrival_time: datetime
    price: float
    currency: str = "USD"
    stops: int = 0
    segments: List[FlightSegment] = Field(default_factory=list)
    seats_remaining: Optional[int] = 9


class FlightStatus(BaseModel):
    """Real-time flight status and disruption monitor."""

    flight_number: str
    status: str = "scheduled"  # scheduled, on_time, delayed, cancelled, diverted
    delay_minutes: int = 0
    gate: Optional[str] = None
    terminal: Optional[str] = None
    estimated_departure: Optional[datetime] = None
    disruption_risk: str = "low"  # low, medium, high
