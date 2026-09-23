"""Flight cancellation emergency recovery workflow."""

from typing import Any, Dict
from app.agent.state import DisruptionEvent


def handle_flight_cancellation(event: DisruptionEvent) -> Dict[str, Any]:
    """Execute emergency protocol when a flight is cancelled."""
    flight = event.flight_number or "Scheduled Flight"
    return {
        "workflow": "flight_cancellation",
        "flight_number": flight,
        "status": "emergency_recovery_active",
        "advisory": f"{flight} has been cancelled by airline. Activating instant guardian rebooking.",
        "actions_taken": [
            "Identify top 3 alternate non-stop and one-stop departures within 6 hours",
            "Hold provisional seat reservation on nearest carrier",
            "Initiate airline statutory compensation/refund claims",
            "Notify traveler via Push, SMS, and WhatsApp",
        ],
        "estimated_resolution_mins": 15,
    }
