"""Core LangChain AI Travel Concierge & Guardian agent runner."""

import logging
from typing import List
from app.core.config import settings
from app.agent.prompts import CONCIERGE_SYSTEM_PROMPT
from app.agent.tools import ALL_TOOLS
from app.agent.state import AgentState, DisruptionEvent
from app.schemas.agent import (
    AgentQueryRequest,
    AgentQueryResponse,
    TravelSafetyAlert,
)

logger = logging.getLogger("TravelConciergeAgent")


class TravelConciergeAgent:
    """Orchestrates LLM calls, tool execution, and guardian safety checks."""

    def __init__(self) -> None:
        self.openai_key = settings.OPENAI_API_KEY
        self.model_name = settings.OPENAI_MODEL
        self.tools = ALL_TOOLS
        self._llm = None
        self._initialize_llm()

    def _initialize_llm(self) -> None:
        """Initialize LangChain ChatOpenAI if API key is present."""
        if self.openai_key:
            try:
                from langchain_openai import ChatOpenAI

                self._llm = ChatOpenAI(
                    model=self.model_name,
                    api_key=self.openai_key,
                    temperature=0.7,
                )
                logger.info("LangChain ChatOpenAI initialized with model: %s", self.model_name)
            except Exception as e:
                logger.warning("Failed to initialize ChatOpenAI: %s. Falling back to local guardian.", e)
                self._llm = None
        else:
            logger.info("OPENAI_API_KEY not configured. Running in local Smart Guardian mode.")

    async def run(self, request: AgentQueryRequest) -> AgentQueryResponse:
        """Process user query and return concierge reply with safety alerts."""
        prompt_lower = request.prompt.lower()

        safety_alerts: List[TravelSafetyAlert] = []
        if "weather" in prompt_lower or "rain" in prompt_lower or "storm" in prompt_lower:
            safety_alerts.append(
                TravelSafetyAlert(
                    level="info",
                    category="weather",
                    title="Weather Advisory Active",
                    description="Variable weather forecasted in destination region. Pack a light umbrella.",
                    recommended_action="Check hourly forecasts prior to outdoor excursions.",
                )
            )
        elif "flight" in prompt_lower or "airport" in prompt_lower or "delay" in prompt_lower:
            safety_alerts.append(
                TravelSafetyAlert(
                    level="info",
                    category="transit",
                    title="Airport Transit Buffer",
                    description="Standard international flight check-in requires 3-hour airport arrival.",
                    recommended_action="Ensure passport is valid for at least 6 months past return date.",
                )
            )

        suggested_actions = [
            "Explore recommended accommodations",
            "Generate custom day-by-day itinerary",
            "Review destination safety guidelines",
        ]

        if self._llm is not None:
            try:
                from langchain_core.messages import HumanMessage, SystemMessage

                messages = [SystemMessage(content=CONCIERGE_SYSTEM_PROMPT)]
                for msg in request.history[-5:]:
                    if msg.role == "user":
                        messages.append(HumanMessage(content=msg.content))
                messages.append(HumanMessage(content=request.prompt))

                response = await self._llm.ainvoke(messages)
                reply_text = str(response.content)
            except Exception as err:
                logger.error("Error invoking LLM agent: %s", err)
                reply_text = self._generate_fallback_response(request.prompt)
        else:
            reply_text = self._generate_fallback_response(request.prompt)

        return AgentQueryResponse(
            reply=reply_text,
            suggested_actions=suggested_actions,
            safety_alerts=safety_alerts,
            sources=["AI Concierge Core", "Smart Travel Guardian Engine"],
            metadata={"model": self.model_name if self._llm else "local-guardian-fallback"},
        )

    def _generate_fallback_response(self, prompt: str) -> str:
        """Heuristic fallback reply providing helpful concierge guidance."""
        return (
            f"Hello! As your AI Travel Concierge & Smart Travel Guardian, I have received your request: "
            f"\"{prompt}\".\n\n"
            f"Here are my initial concierge recommendations:\n"
            f"• Optimal travel timing: Shoulder season provides mild weather and lower crowds.\n"
            f"• Safety status: Destination safety is normal with standard vigilance.\n"
            f"• Accommodation: Central district stays recommended for accessibility.\n\n"
            f"Configure `OPENAI_API_KEY` in `.env` to unlock live multi-tool LangChain autonomous reasoning!"
        )


travel_concierge_agent = TravelConciergeAgent()
