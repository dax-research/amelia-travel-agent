"""Tests for hotel search endpoints."""


def test_hotel_search(client):
    """Verify hotel accommodations search endpoint."""
    search_res = client.get(
        "/api/hotels/search",
        params={
            "city": "Barcelona",
            "check_in": "2026-08-01",
            "check_out": "2026-08-05",
            "guests": 2,
        },
    )
    assert search_res.status_code == 200
    hotels = search_res.json()["data"]
    assert len(hotels) >= 1
    assert "Barcelona" in hotels[0]["city"]
