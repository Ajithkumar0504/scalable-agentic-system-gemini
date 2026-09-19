from fastapi import FastAPI
from models import ChatRequest, ChatResponse
from agent import Agent

app = FastAPI(
    title="Scalable Agentic System",
    description="Fresher-friendly Gemini Agentic AI project",
    version="1.0.0",
)

agent = Agent()


@app.get("/")
def home():
    return {
        "message": "Scalable Agentic System is running."
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    result = agent.chat(request.message)

    return ChatResponse(
        message=result["message"],
        selected_tool=result["selected_tool"],
        result=result["result"],
    )
