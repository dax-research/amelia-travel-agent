"""Dynamic itinerary schedule adjustment workflow for weather disruptions and delays."""

from typing import Any, Dict
from app.agent.state import DisruptionEvent


def handle_weather_disruption(event: DisruptionEvent) -> Dict[str, Any]:
    """Dynamically swap outdoor activities with premium indoor alternatives during severe weather."""
    location = event.details.get("location", "Destination")
    condition = event.details.get("condition", "Heavy Storm")

    return {
        "workflow": "itinerary_replanning",
        "hazard_type": "weather",
        "location": location,
        "advisory": f"Severe weather ({condition}) detected in {location}. Rescheduling outdoor excursions.",
        "actions_taken": [
            "Moved outdoor walking tours to later in the week",
            "Substituted with indoor art gallery & culinary masterclass",
            "Notified tour guides of reschedule",
        ],
    }
