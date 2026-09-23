"""AI Travel Concierge & Guardian interaction endpoints."""

from fastapi import APIRouter
from app.agent.agent import travel_concierge_agent
from app.schemas.agent import AgentQueryRequest, AgentQueryResponse
from app.schemas.common import ApiResponse

router = APIRouter(prefix="/agent", tags=["AI Agent"])


@router.post(
    "/query",
    response_model=ApiResponse[AgentQueryResponse],
    summary="Chat with the AI Travel Concierge & Smart Guardian",
)
async def query_agent(payload: AgentQueryRequest) -> ApiResponse[AgentQueryResponse]:
    """Process traveler instructions, queries, and itinerary requests with real-time guardian oversight."""
    response = await travel_concierge_agent.run(payload)
    return ApiResponse(
        success=True,
        message="Agent response generated successfully.",
        data=response,
    )
