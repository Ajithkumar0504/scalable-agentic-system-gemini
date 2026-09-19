from tool_registry import TOOLS


def system_search(query: str):
    query = query.lower()

    matches = []

    for tool in TOOLS:
        searchable_text = (
            tool["name"] + " " +
            tool["description"] + " " +
            tool["category"]
        ).lower()

        if any(word in searchable_text for word in query.split()):
            matches.append({
                "name": tool["name"],
                "description": tool["description"],
                "category": tool["category"],
            })

    if not matches:
        return {
            "status": "success",
            "tools": []
        }

    return {
        "status": "success",
        "tools": matches
    }
