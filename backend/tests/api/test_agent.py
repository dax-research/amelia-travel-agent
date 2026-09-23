"""Tests for AI concierge agent endpoint."""


def test_agent_query(client):
    """Verify conversational AI concierge endpoint."""
    res = client.post(
        "/api/agent/query",
        json={"prompt": "What are the top 3 safety tips for traveling to Tokyo in Autumn?"},
    )
    assert res.status_code == 200
    data = res.json()["data"]
    assert "reply" in data
    assert len(data["suggested_actions"]) > 0
