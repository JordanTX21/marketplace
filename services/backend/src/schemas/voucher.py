from typing import Optional
from pydantic import BaseModel

class Voucher(BaseModel):
    id: Optional[str] = None
    type: str
    method_payment: str
    amount: float
    state: Optional[str] = None
    order_id: int
    