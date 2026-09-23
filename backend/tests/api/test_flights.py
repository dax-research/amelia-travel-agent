"""Tests for flight search and status endpoints."""


def test_flight_search_and_status(client):
    """Verify flight querying and live status probe."""
    search_res = client.get(
        "/api/flights/search",
        params={
            "origin": "JFK",
            "destination": "LHR",
            "departure_date": "2026-09-01",
            "passengers": 1,
        },
    )
    assert search_res.status_code == 200
    offers = search_res.json()["data"]
    assert len(offers) >= 1
    assert offers[0]["origin"] == "JFK"

    status_res = client.get("/api/flights/status/SK101")
    assert status_res.status_code == 200
    status_data = status_res.json()["data"]
    assert status_data["flight_number"] == "SK101"
    assert "status" in status_data
