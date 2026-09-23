"""Missed flight connection recovery and layover hospitality workflow."""

from typing import Any, Dict
from app.agent.state import DisruptionEvent


def handle_missed_connection(event: DisruptionEvent) -> Dict[str, Any]:
    """Execute recovery protocol for missed connecting flights."""
    connecting_flight = event.details.get("connecting_flight", "Onward Connection")
    transit_city = event.details.get("transit_city", "Transit Hub")

    return {
        "workflow": "missed_connection",
        "connecting_flight": connecting_flight,
        "transit_city": transit_city,
        "status": "connection_replanning_active",
        "advisory": f"Connection missed at {transit_city}. Arranging next morning departure and transit hotel.",
        "actions_taken": [
            f"Auto-rebooked on morning departure {connecting_flight}",
            f"Generated transit hotel voucher near {transit_city} airport",
            "Updated destination hotel check-in date to tomorrow",
            "Adjusted Day 1 itinerary activities forward",
        ],
    }
