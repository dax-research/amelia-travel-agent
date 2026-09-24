from app.agent.agent import TravelAgent
from app.agent.state import AgentState


def main():
    state = AgentState(
        traveler_id="traveler_001",
        trip_id="trip_001",
        current_itinerary={
            "route": "AMD → DEL → FRA",
            "status": "disrupted",
        },
        disruption={
            "type": "flight_cancellation",
            "flight_number": "AI999",
            "origin": "AMD",
            "destination": "DEL",
        },
    )

    agent = TravelAgent()

    final_state = agent.run(state)

    print("\nFinal state:")
    print(final_state)


if __name__ == "__main__":
    main()