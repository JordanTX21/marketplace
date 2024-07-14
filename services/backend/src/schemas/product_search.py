from typing import Optional
from pydantic import BaseModel

class ProductSearch(BaseModel):
    id: Optional[str] = None
    name: str
    user_id: Optional[int] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    order_by: Optional[str] = None