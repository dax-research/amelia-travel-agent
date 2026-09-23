"""Tests for trip management endpoints."""

from app.core.security import create_access_token


def test_create_and_list_trips(client):
    """Verify trip creation and listing for authenticated user."""
    token = create_access_token(subject="usr_trip_test")
    headers = {"Authorization": f"Bearer {token}"}

    payload = {
        "destination": "Paris, France",
        "origin": "JFK",
        "start_date": "2026-07-10",
        "end_date": "2026-07-17",
        "travelers_count": 2,
        "budget": 4500.0,
        "preferences": ["art", "culinary"],
    }
    create_res = client.post("/api/trips", json=payload, headers=headers)
    assert create_res.status_code == 201
    trip_data = create_res.json()["data"]
    assert trip_data["destination"] == "Paris, France"
    trip_id = trip_data["id"]

    list_res = client.get("/api/trips", headers=headers)
    assert list_res.status_code == 200
    assert len(list_res.json()["data"]) >= 1

    detail_res = client.get(f"/api/trips/{trip_id}", headers=headers)
    assert detail_res.status_code == 200
    assert detail_res.json()["data"]["id"] == trip_id
