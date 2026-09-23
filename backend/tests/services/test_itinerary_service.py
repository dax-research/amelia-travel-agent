"""Unit tests for itinerary service business logic."""

from app.schemas.itinerary import ItineraryGenerateRequest, ItineraryItemCreate
from app.services.itinerary_service import itinerary_service


def test_itinerary_service_generation():
    """Verify multi-day itinerary generation and item appending."""
    req = ItineraryGenerateRequest(
        trip_id="trip_svc_test",
        destination="London, UK",
        days=3,
        interests=["museums", "parks"],
    )
    itin = itinerary_service.generate_itinerary(req)
    assert itin.total_days == 3
    assert len(itin.days) == 3

    item = ItineraryItemCreate(
        time="16:00",
        title="Tower of London Visit",
        category="activity",
    )
    updated = itinerary_service.add_item_to_day("trip_svc_test", 2, item)
    day_2_titles = [i.title for i in updated.days[1].items]
    assert "Tower of London Visit" in day_2_titles
