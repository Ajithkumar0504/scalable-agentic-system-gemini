DOCUMENTS = {
    "invoice": (
        "Invoice policy: an invoice contains customer information, "
        "amount and currency. The invoice should be validated before creation."
    ),
    "payment": (
        "Payment guide: payments require a customer, amount and currency. "
        "The amount must be greater than zero."
    ),
    "dispute": (
        "Dispute guide: a dispute can be checked using the customer user ID."
    ),
}


def rag_search(question: str):
    question = question.lower()

    matches = []

    for keyword, document in DOCUMENTS.items():
        if keyword in question:
            matches.append(document)

    if not matches:
        return "No relevant information was found in the knowledge base."

    return "\n".join(matches)
