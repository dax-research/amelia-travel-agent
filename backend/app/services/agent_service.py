"""Business logic service for AI Agent session coordination."""

from typing import Any, Dict
from app.agent.agent import travel_concierge_agent
from app.schemas.agent import AgentQueryRequest, AgentQueryResponse
from app.services.base import BaseService


class AgentService(BaseService):
    """Manages chat context and dispatches queries to LangChain concierge agent."""

    async def chat(self, request: AgentQueryRequest) -> AgentQueryResponse:
        """Process chat prompt and return autonomous concierge response."""
        self.log_action("agent_query_processed", {"trip_id": request.trip_id})
        return await travel_concierge_agent.run(request)


agent_service = AgentService()
