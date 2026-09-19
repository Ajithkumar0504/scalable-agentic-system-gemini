TOOLS = [
    {
        "name": "create_invoice",
        "description": "Create an invoice for a customer.",
        "category": "invoice",
    },
    {
        "name": "send_payment",
        "description": "Send a payment to a customer.",
        "category": "payment",
    },
    {
        "name": "get_sales_report",
        "description": "Get total sales volume for a period.",
        "category": "report",
    },
    {
        "name": "get_dispute",
        "description": "Check whether a customer has an open dispute.",
        "category": "dispute",
    },
    {
        "name": "refund_payment",
        "description": "Refund a payment.",
        "category": "payment",
    },
]


def get_tool_names():
    return [tool["name"] for tool in TOOLS]


def search_tools(keyword: str):
    keyword = keyword.lower()

    results = []

    for tool in TOOLS:
        text = (
            tool["name"] + " " +
            tool["description"] + " " +
            tool["category"]
        ).lower()

        if keyword in text:
            results.append(tool)

    return results
