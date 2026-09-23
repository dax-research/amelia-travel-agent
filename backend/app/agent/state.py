"""LangChain and LangGraph agent state definitions."""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class DisruptionEvent(BaseModel):
    """Event model representing detected travel disruptions."""

    event_id: str
    event_type: str  # flight_delay, flight_cancellation, missed_connection, severe_weather
    severity: str = "warning"  # info, warning, critical
    flight_number: Optional[str] = None
    delay_minutes: int = 0
    details: Dict[str, Any] = Field(default_factory=dict)


class AgentState(BaseModel):
    """Runtime state of the autonomous travel concierge and guardian."""

    session_id: str
    user_id: Optional[str] = None
    current_trip_id: Optional[str] = None
    messages: List[Dict[str, Any]] = Field(default_factory=list)
    active_disruptions: List[DisruptionEvent] = Field(default_factory=list)
    recommended_itinerary_updates: List[Dict[str, Any]] = Field(default_factory=list)
    context_data: Dict[str, Any] = Field(default_factory=dict)
