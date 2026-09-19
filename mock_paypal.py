from datetime import datetime


def create_invoice(customer, amount, currency="USD"):
    return {
        "status": "success",
        "invoice_id": "INV-1001",
        "customer": customer,
        "amount": amount,
        "currency": currency,
        "message": "Invoice created successfully."
    }


def send_payment(customer, amount, currency="USD"):
    return {
        "status": "success",
        "payment_id": "PAY-2001",
        "customer": customer,
        "amount": amount,
        "currency": currency,
        "message": "Payment sent successfully."
    }


def get_sales_report(month="last_month"):
    return {
        "status": "success",
        "period": month,
        "total_sales": 50000,
        "currency": "USD"
    }


def get_dispute(user_id):
    return {
        "status": "success",
        "user_id": user_id,
        "open_dispute": False,
        "message": "No open dispute found."
    }


def refund_payment(customer, amount, currency="USD"):
    return {
        "status": "success",
        "refund_id": "REF-3001",
        "customer": customer,
        "amount": amount,
        "currency": currency,
        "message": "Payment refunded successfully.",
        "time": datetime.now().isoformat()
    }
