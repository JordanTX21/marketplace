from typing import Optional, List
from pydantic import BaseModel

class Product(BaseModel):
    id: Optional[int] = None
    quantity: int
    amount: float

class Order(BaseModel):
    id: Optional[int] = None
    quantity: int
    amount: float
    client_id: int
    user_id: int
    products: List[Product]