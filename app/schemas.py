# app/schemas.py

import enum
from uuid import UUID
from pydantic import BaseModel
from typing import List, Optional


class RoleEnum(enum.Enum):
    ADMIN = "admin"
    MODERATOR = "moderator"
    USER = "user"


class User(BaseModel):
    id: UUID
    username: str
    full_name: str
    email: str
    phone: str
    password: str
    role: RoleEnum

    class Config:
        orm_mode = True


class Consumer(BaseModel):
    username: str
    full_name: str
    phone: str
    email: str

    class Config:
        orm_mode = True


class Event(BaseModel):
    name: str
    description: Optional[str] = None
    data: Optional[str] = None

    class Config:
        orm_mode = True


class Ticket(BaseModel):
    price: float
    ticket_category_id: int
    ticket_name: Optional[str] = None

    class Config:
        orm_mode = True


class TicketCategories(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class Hall(BaseModel):
    name: str

    class Config:
        orm_mode = True


class City(BaseModel):
    id: int
    name: str
    state: str

    class Config:
        orm_mode = True
