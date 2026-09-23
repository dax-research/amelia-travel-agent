"""Unit tests for trip service business logic."""

from datetime import date
from app.schemas.trip import TripCreate
from app.services.trip_service import trip_service


def test_trip_service_creation_and_lookup():
    """Verify trip creation populates initial itinerary day and can be retrieved."""
    user_id = "usr_unit_test_99"
    payload = TripCreate(
        destination="Kyoto, Japan",
        start_date=date(2026, 11, 1),
        end_date=date(2026, 11, 8),
        travelers_count=2,
    )
    trip = trip_service.create_trip(user_id=user_id, payload=payload)
    assert trip.id.startswith("trip_")
    assert trip.destination == "Kyoto, Japan"
    assert len(trip.itinerary) >= 1

    fetched = trip_service.get_trip(user_id=user_id, trip_id=trip.id)
    assert fetched.id == trip.id
