"""Central travel disruption orchestrator workflow."""

import logging
from typing import Any, Dict
from app.agent.state import DisruptionEvent

logger = logging.getLogger("DisruptionWorkflow")


class DisruptionOrchestrator:
    """Classifies travel disruptions and triggers appropriate mitigation workflows."""

    def evaluate_event(self, event: DisruptionEvent) -> Dict[str, Any]:
        """Triage the disruption event and route to specialized mitigation handler."""
        logger.info("Evaluating disruption event: %s (%s)", event.event_id, event.event_type)

        if event.event_type == "flight_delay":
            from app.agent.workflows.flight_delay import handle_flight_delay
            return handle_flight_delay(event)

        elif event.event_type == "flight_cancellation":
            from app.agent.workflows.flight_cancellation import handle_flight_cancellation
            return handle_flight_cancellation(event)

        elif event.event_type == "missed_connection":
            from app.agent.workflows.missed_connection import handle_missed_connection
            return handle_missed_connection(event)

        elif event.event_type == "weather_hazard":
            from app.agent.workflows.itinerary_replanning import handle_weather_disruption
            return handle_weather_disruption(event)

        return {
            "status": "logged",
            "message": f"Disruption {event.event_type} logged with standard vigilance.",
            "actions_taken": [],
        }


disruption_orchestrator = DisruptionOrchestrator()
