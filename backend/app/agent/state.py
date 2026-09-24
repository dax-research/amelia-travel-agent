from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentState:
    traveler_id: str | None = None
    trip_id: str | None = None

    current_itinerary: dict[str, Any] = field(default_factory=dict)
    disruption: dict[str, Any] = field(default_factory=dict)

    candidate_flights: list[dict[str, Any]] = field(default_factory=list)

    selected_flight: dict[str, Any] | None = None

    action: str | None = None
    status: str = "started"

    messages: list[dict[str, Any]] = field(default_factory=list)