from typing import Any

from app.agent.state import AgentState
from app.agent.tools import search_flights


class TravelAgent:
    def __init__(self):
        self.tools = {
            "search_flights": search_flights,
        }

    def execute_tool(
        self,
        tool_name: str,
        arguments: dict[str, Any],
    ) -> Any:
        """
        Execute a tool requested by the agent.
        """

        if tool_name not in self.tools:
            raise ValueError(f"Unknown tool: {tool_name}")

        tool = self.tools[tool_name]

        return tool(**arguments)

    def run(self, state: AgentState) -> AgentState:
        """
        Run the travel agent.

        For now this uses a deterministic mock decision.
        Later this method will contain the real LLM agent loop.
        """

        state.status = "running"

        print("\n--- Agent started ---")

        print("Current disruption:")
        print(state.disruption)

        # Temporary mock decision.
        #
        # Later:
        # LLM → tool call → execute tool → result → LLM

        tool_name = "search_flights"

        arguments = {
            "origin": state.disruption["origin"],
            "destination": state.disruption["destination"],
        }

        print(f"\nAgent decided to call: {tool_name}")
        print(f"Arguments: {arguments}")

        result = self.execute_tool(
            tool_name,
            arguments,
        )

        print("\nTool result:")
        print(result)

        state.candidate_flights = result
        state.action = "evaluate_flights"
        state.status = "waiting_for_evaluation"

        print("\n--- Agent finished step ---")

        return state