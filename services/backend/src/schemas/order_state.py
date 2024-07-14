from typing import Optional, List
from pydantic import BaseModel

class OrderState(BaseModel):
    id: Optional[str] = None
    state: str