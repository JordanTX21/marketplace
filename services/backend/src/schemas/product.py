from typing import Optional, List
from pydantic import BaseModel

class Product(BaseModel):
    id: Optional[str] = None
    code: Optional[str] = None
    name: str
    description: str
    price: float
    min_stock: int
    user_id: int
    images: Optional[List[str]] = None
    categories: Optional[List[str]] = None