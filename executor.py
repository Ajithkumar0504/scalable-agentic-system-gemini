from models import (
    InvoiceRequest,
    PaymentRequest,
    DisputeRequest,
    SalesReportRequest,
)
from mock_paypal import (
    create_invoice,
    send_payment,
    get_sales_report,
    get_dispute,
    refund_payment,
)


def execute_tool(decision):

    if decision.tool_name == "create_invoice":
        request = InvoiceRequest(
            customer=decision.customer or "Unknown",
            amount=decision.amount or 0,
            currency=decision.currency or "USD",
        )
        return create_invoice(
            request.customer,
            request.amount,
            request.currency,
        )

    if decision.tool_name == "send_payment":
        request = PaymentRequest(
            customer=decision.customer or "Unknown",
            amount=decision.amount or 0,
            currency=decision.currency or "USD",
        )
        return send_payment(
            request.customer,
            request.amount,
            request.currency,
        )

    if decision.tool_name == "get_sales_report":
        request = SalesReportRequest(
            month=decision.month or "last_month"
        )
        return get_sales_report(request.month)

    if decision.tool_name == "get_dispute":
        request = DisputeRequest(
            user_id=decision.user_id or "unknown"
        )
        return get_dispute(request.user_id)

    if decision.tool_name == "refund_payment":
        request = PaymentRequest(
            customer=decision.customer or "Unknown",
            amount=decision.amount or 0,
            currency=decision.currency or "USD",
        )
        return refund_payment(
            request.customer,
            request.amount,
            request.currency,
        )

    return {
        "status": "error",
        "message": "Tool not found."
    }
