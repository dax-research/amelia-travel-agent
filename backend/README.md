# AI Travel Concierge & Smart Travel Guardian - Backend

An autonomous AI-powered Travel Concierge and real-time Smart Travel Guardian backend built with **FastAPI**, **LangChain**, and **Pydantic v2**.

---

## Directory Structure

```text
backend/
│
├── app/
│   │
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── security.py
│   │   └── dependencies.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── router.py
│   │   │
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── health.py
│   │       ├── auth.py
│   │       ├── users.py
│   │       ├── trips.py
│   │       ├── itinerary.py
│   │       ├── flights.py
│   │       ├── hotels.py
│   │       ├── bookings.py
│   │       ├── notifications.py
│   │       └── agent.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── common.py
│   │   ├── auth.py
│   │   ├── user.py
│   │   ├── trip.py
│   │   ├── itinerary.py
│   │   ├── flight.py
│   │   ├── hotel.py
│   │   ├── booking.py
│   │   ├── notification.py
│   │   └── agent.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── user_service.py
│   │   ├── trip_service.py
│   │   ├── itinerary_service.py
│   │   ├── flight_service.py
│   │   ├── hotel_service.py
│   │   ├── booking_service.py
│   │   ├── notification_service.py
│   │   └── agent_service.py
│   │
│   ├── agent/
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   ├── state.py
│   │   ├── prompts.py
│   │   │
│   │   ├── tools/
│   │   │   ├── __init__.py
│   │   │   ├── flight_tools.py
│   │   │   ├── hotel_tools.py
│   │   │   ├── booking_tools.py
│   │   │   ├── itinerary_tools.py
│   │   │   ├── activity_tools.py
│   │   │   ├── weather_tools.py
│   │   │   └── notification_tools.py
│   │   │
│   │   └── workflows/
│   │       ├── __init__.py
│   │       ├── disruption.py
│   │       ├── flight_delay.py
│   │       ├── flight_cancellation.py
│   │       ├── missed_connection.py
│   │       └── itinerary_replanning.py
│   │
│   ├── integrations/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   │
│   │   ├── flights/
│   │   │   ├── __init__.py
│   │   │   └── flight_provider.py
│   │   │
│   │   ├── hotels/
│   │   │   ├── __init__.py
│   │   │   └── hotel_provider.py
│   │   │
│   │   ├── maps/
│   │   │   ├── __init__.py
│   │   │   └── maps_provider.py
│   │   │
│   │   ├── weather/
│   │   │   ├── __init__.py
│   │   │   └── weather_provider.py
│   │   │
│   │   └── notifications/
│   │       ├── __init__.py
│   │       └── notification_provider.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── helpers.py
│       └── exceptions.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   │
│   ├── api/
│   │   ├── test_health.py
│   │   ├── test_auth.py
│   │   ├── test_trips.py
│   │   ├── test_itinerary.py
│   │   ├── test_flights.py
│   │   ├── test_hotels.py
│   │   └── test_agent.py
│   │
│   ├── services/
│   │   ├── test_trip_service.py
│   │   ├── test_itinerary_service.py
│   │   └── test_agent_service.py
│   │
│   └── agent/
│       ├── test_tools.py
│       └── test_workflows.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Architectural Highlights

### 1. API Routing Layer (`app/api/v1/`)
- **`health.py`**: Operational health probes.
- **`auth.py`**: User registration and JWT issuance.
- **`users.py`**: Profile management and travel preferences.
- **`trips.py`**: Trip creation and tracking.
- **`itinerary.py`**: Day-by-day itinerary generation and item manipulation.
- **`flights.py`**: Flight search and live status tracking.
- **`hotels.py`**: Hotel accommodations and room rates.
- **`bookings.py`**: Unified booking transaction management.
- **`notifications.py`**: Guardian alerts and advisory dispatches.
- **`agent.py`**: Conversational endpoint with AI Concierge and Guardian.

### 2. Autonomous Agent & Workflows (`app/agent/`)
- **`agent.py` & `state.py`**: LangChain orchestration pipeline maintaining session context and disruption state.
- **`tools/`**: Dedicated tools for flight search, hotel reservations, activity suggestions, weather checks, itinerary construction, and safety alerts.
- **`workflows/`**: Autonomous disruption response workflows:
  - `disruption.py`: Central triage router.
  - `flight_delay.py`: Buffer assessment and connection protection.
  - `flight_cancellation.py`: Instant rebooking on alternate flights.
  - `missed_connection.py`: Layover hotel accommodation and transit rebooking.
  - `itinerary_replanning.py`: Dynamic reschedule of excursions during adverse weather.

### 3. Integrations (`app/integrations/`)
Structured provider clients for flights (Amadeus), hotels, maps (Google Places), weather (OpenWeatherMap), and multichannel notifications.

---

## Setup & Running Locally

### 1. Prerequisites
- Python 3.10+
- Virtual environment tool (`venv` or `uv`)

### 2. Install Dependencies
```powershell
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 3. Environment Configuration
```powershell
cp .env.example .env
```
Add optional API keys for `OPENAI_API_KEY`, `WEATHER_API_KEY`, or `AMADEUS_API_KEY`.

### 4. Run Development Server
```powershell
uvicorn app.main:app --reload --port 8000
```
- **API Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Health Check**: [http://localhost:8000/health](http://localhost:8000/health)

---

## Testing

Run all automated unit and integration tests:
```powershell
pytest
```
Or run specific test suites:
```powershell
pytest tests/api
pytest tests/services
pytest tests/agent
```
