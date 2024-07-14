from typing import Optional
from pydantic import BaseModel

class Client(BaseModel):
    id: Optional[int] = None
    type_document: str
    document: str
    name: str
    address: str
    email: str
    user_id: int