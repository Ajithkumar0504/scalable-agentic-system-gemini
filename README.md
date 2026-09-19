# Scalable Agentic System with Gemini API

A fresher-friendly implementation of the Datazoic "Design a Scalable Agentic System" task.

## What this project demonstrates

- Natural-language user request
- Gemini API for intent/tool selection
- Tool registry
- Tool routing
- PayPal-like mock tools
- Multi-step tool execution
- RAG knowledge search tool
- System search tool
- Pydantic parameter validation
- Error handling
- FastAPI REST API
- Simple conversation state
- Easy path to scaling from 50 to 500+ tools

## Architecture

User -> FastAPI -> Gemini Router -> Tool Search -> Tool Executor -> Response

Special routes:
- RAG questions -> RAG tool
- System/tool questions -> System Search tool

## Setup

1. Create a virtual environment.

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install packages:

```bash
pip install -r requirements.txt
```

3. Create `.env` from `.env.example`.

4. Add your Gemini API key:

```env
GEMINI_API_KEY=your_key
GEMINI_MODEL=gemini-2.5-flash
```

5. Run:

```bash
uvicorn main:app --reload
```

6. Open:

http://127.0.0.1:8000/docs

## Example requests

POST `/chat`

```json
{
  "message": "Create an invoice for John for 50 dollars"
}
```

```json
{
  "message": "What was my total sales volume last month?"
}
```

```json
{
  "message": "Is there a dispute open from user_123?"
}
```

```json
{
  "message": "What tools are available for invoices?"
}
```

```json
{
  "message": "What is the invoice policy?"
}
```

## Important

This project uses MOCK PayPal APIs. It does not send real money or call real PayPal services.

For a production system, replace `mock_paypal.py` with authenticated API calls, add a real vector database for semantic tool retrieval, persistent state, authentication, rate limits, approval workflows, and observability.
