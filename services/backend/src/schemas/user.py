from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[str] = None
    name: str
    email: str
    password: str
    repeatPassword: str = None
    photo: Optional[str] = None
    description: Optional[str] = None