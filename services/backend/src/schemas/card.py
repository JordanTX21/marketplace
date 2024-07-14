from typing import Optional
from pydantic import BaseModel

class Card(BaseModel):
    id: Optional[int] = None
    name: str
    number: str
    month: str
    year: str
    cvv: str
    user_id: int