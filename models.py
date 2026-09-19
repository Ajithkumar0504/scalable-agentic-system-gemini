from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List


class ChatRequest(BaseModel):
    message: str = Field(min_length=1)


class ChatResponse(BaseModel):
    message: str
    selected_tool: Optional[str] = None
    result: Any = None


class InvoiceRequest(BaseModel):
    customer: str = Field(min_length=1)
    amount: float = Field(gt=0)
    currency: str = "USD"


class PaymentRequest(BaseModel):
    customer: str = Field(min_length=1)
    amount: float = Field(gt=0)
    currency: str = "USD"


class DisputeRequest(BaseModel):
    user_id: str = Field(min_length=1)


class SalesReportRequest(BaseModel):
    month: str = "last_month"


class RouterDecision(BaseModel):
    route: str
    tool_name: Optional[str] = None
    customer: Optional[str] = None
    amount: Optional[float] = None
    currency: Optional[str] = "USD"
    user_id: Optional[str] = None
    month: Optional[str] = "last_month"
