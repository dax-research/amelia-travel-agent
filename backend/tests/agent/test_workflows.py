"""Unit tests for travel disruption workflows."""

from app.agent.state import DisruptionEvent
from app.agent.workflows.disruption import disruption_orchestrator
from app.agent.workflows.flight_delay import handle_flight_delay
from app.agent.workflows.flight_cancellation import handle_flight_cancellation
from app.agent.workflows.missed_connection import handle_missed_connection
from app.agent.workflows.itinerary_replanning import handle_weather_disruption


def test_flight_delay_workflow():
    """Verify flight delay severity classification and actions."""
    minor_event = DisruptionEvent(
        event_id="ev_001",
        event_type="flight_delay",
        flight_number="SK101",
        delay_minutes=30,
    )
    res_minor = handle_flight_delay(minor_event)
    assert res_minor["severity"] == "low"

    major_event = DisruptionEvent(
        event_id="ev_002",
        event_type="flight_delay",
        flight_number="SK101",
        delay_minutes=150,
    )
    res_major = handle_flight_delay(major_event)
    assert res_major["severity"] == "high"
    assert len(res_major["actions_taken"]) >= 2


def test_flight_cancellation_workflow():
    """Verify flight cancellation triggers emergency protocol."""
    event = DisruptionEvent(
        event_id="ev_003",
        event_type="flight_cancellation",
        flight_number="SK202",
    )
    res = handle_flight_cancellation(event)
    assert res["status"] == "emergency_recovery_active"
    assert len(res["actions_taken"]) > 0


def test_missed_connection_and_weather_workflows():
    """Verify missed connection and weather replanning workflows."""
    missed_ev = DisruptionEvent(
        event_id="ev_004",
        event_type="missed_connection",
        details={"connecting_flight": "LH450", "transit_city": "Frankfurt"},
    )
    res_missed = handle_missed_connection(missed_ev)
    assert res_missed["workflow"] == "missed_connection"

    weather_ev = DisruptionEvent(
        event_id="ev_005",
        event_type="weather_hazard",
        details={"location": "Geneva", "condition": "Severe Thunderstorm"},
    )
    res_weather = handle_weather_disruption(weather_ev)
    assert res_weather["hazard_type"] == "weather"
