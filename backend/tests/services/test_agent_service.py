"""Unit tests for agent service business logic."""

import pytest
from app.schemas.agent import AgentQueryRequest
from app.services.agent_service import agent_service


@pytest.mark.asyncio
async def test_agent_service_chat():
    """Verify agent service returns structured response with actions and alerts."""
    req = AgentQueryRequest(
        prompt="Check weather and plan day in Zurich",
        trip_id="trip_agent_svc",
    )
    res = await agent_service.chat(req)
    assert res.reply is not None
    assert len(res.suggested_actions) > 0
    assert "model" in res.metadata
