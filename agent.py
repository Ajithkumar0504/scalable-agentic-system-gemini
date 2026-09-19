from gemini_router import route_with_gemini
from executor import execute_tool
from rag_tool import rag_search
from system_search import system_search


class Agent:

    def __init__(self):
        self.history = []

    def chat(self, user_message: str):

        self.history.append({
            "role": "user",
            "message": user_message
        })

        try:
            decision = route_with_gemini(user_message)

            if decision.route == "rag":
                result = rag_search(user_message)

                return {
                    "message": result,
                    "selected_tool": "rag_tool",
                    "result": result,
                }

            if decision.route == "system_search":
                result = system_search(user_message)

                return {
                    "message": "System search completed.",
                    "selected_tool": "system_search",
                    "result": result,
                }

            if decision.route == "api":
                result = execute_tool(decision)

                return {
                    "message": "API tool executed successfully.",
                    "selected_tool": decision.tool_name,
                    "result": result,
                }

            return {
                "message": "I could not understand the request.",
                "selected_tool": None,
                "result": None,
            }

        except Exception as error:
            return {
                "message": "An error occurred while processing the request.",
                "selected_tool": None,
                "result": str(error),
            }
