import json
from google import genai

from config import GEMINI_API_KEY, GEMINI_MODEL
from models import RouterDecision
from tool_registry import TOOLS

client = genai.Client(api_key=GEMINI_API_KEY)


def route_with_gemini(user_message: str) -> RouterDecision:
    tool_summary = json.dumps(TOOLS, indent=2)

    prompt = f'''
You are a simple routing agent.

Available tools:
{tool_summary}

User request:
{user_message}

Choose exactly one route:
- api: use one of the listed API tools
- rag: user is asking for documentation, policy, guide, or knowledge
- system_search: user is asking what tools/capabilities exist or asking about system status
- unknown: request is unclear

If route is api, choose the best tool.

Extract parameters when possible:
- customer
- amount
- currency
- user_id
- month

Return ONLY valid JSON with this structure:
{{
  "route": "api|rag|system_search|unknown",
  "tool_name": "tool name or null",
  "customer": "customer or null",
  "amount": 0,
  "currency": "USD",
  "user_id": "user id or null",
  "month": "last_month"
}}
'''

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config={
            "response_mime_type": "application/json"
        }
    )

    data = json.loads(response.text)
    return RouterDecision(**data)
