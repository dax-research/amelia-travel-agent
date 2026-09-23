"""Tests for itinerary endpoints."""

from app.core.security import create_access_token


def test_itinerary_generation_and_activity_add(client):
    """Verify AI itinerary auto-generation and item insertion."""
    token = create_access_token(subject="usr_itinerary_test")
    headers = {"Authorization": f"Bearer {token}"}

    gen_payload = {
        "trip_id": "trip_itin_101",
        "destination": "Rome, Italy",
        "days": 2,
        "interests": ["history", "coffee"],
    }
    gen_res = client.post("/api/itinerary/generate", json=gen_payload, headers=headers)
    assert gen_res.status_code == 200
    itin_data = gen_res.json()["data"]
    assert itin_data["total_days"] == 2
    assert len(itin_data["days"]) == 2

    # Add custom activity to Day 1
    item_payload = {
        "time": "17:00",
        "title": "Sunset Espresso at Piazza Navona",
        "location": "Piazza Navona",
        "category": "dining",
    }
    add_res = client.post(
        "/api/itinerary/trip_itin_101/days/1/items",
        json=item_payload,
        headers=headers,
    )
    assert add_res.status_code == 201
    updated_days = add_res.json()["data"]["days"]
    assert any(it["title"] == "Sunset Espresso at Piazza Navona" for it in updated_days[0]["items"])
