# app/schemas.py

from pydantic import BaseModel
from typing import List, Optional


class User(BaseModel):
    username: str
    full_name: str

    class Config:
        orm_mode = True


class Event(BaseModel):
    name: str
    description: Optional[str] = None
    data: Optional[str] = None


