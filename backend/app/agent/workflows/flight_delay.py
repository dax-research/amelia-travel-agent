"""Flight delay automated mitigation workflow."""

from typing import Any, Dict
from app.agent.state import DisruptionEvent


def handle_flight_delay(event: DisruptionEvent) -> Dict[str, Any]:
    """Analyze flight delay impact on onward connection and schedule."""
    delay = event.delay_minutes
    flight = event.flight_number or "Scheduled Flight"

    if delay < 45:
        severity = "low"
        advice = f"{flight} delayed by {delay} mins. Connection buffer is sufficient."
        actions = ["Monitor gate updates"]
    elif delay < 120:
        severity = "medium"
        advice = f"{flight} delayed by {delay} mins. Tight connection risk. Alerting airport ground staff."
        actions = ["Notify traveler with priority push", "Check connecting flight minimum connect time"]
    else:
        severity = "high"
        advice = f"{flight} delayed by {delay} mins. Significant disruption. Rebooking alternatives queued."
        actions = [
            "Send urgent SMS & Push to traveler",
            "Hold seats on subsequent connecting departures",
            "Notify arrival hotel of delayed check-in",
        ]

    return {
        "workflow": "flight_delay",
        "flight_number": flight,
        "delay_minutes": delay,
        "severity": severity,
        "advisory": advice,
        "actions_taken": actions,
    }
