# Pydantic schemas for request/response validation

"""
In this code:

    We define a Buyer schema to represent the buyer information.
    We define a TicketSelection schema to represent a single ticket selection, including the event name, ticket details, and buyer information.
    We define a TicketSelectionRequest schema to represent the entire request payload containing multiple ticket selections.

The List[TicketSelection] notation in TicketSelectionRequest indicates that the request payload will contain a list of TicketSelection objects.

These Pydantic schemas will automatically validate incoming JSON data against the specified structure and raise validation errors if the data doesn't match. This ensures that the incoming data is properly formatted before processing it further in the backend.

Next, we can continue by implementing CRUD operations in the crud.py file.
"""
from datetime import datetime

from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import List, Optional
from enum import Enum


# class Role(str, Enum):
#     admin = "admin"
#     moderator = "moderator"
#     user = "user"


class Buyer(BaseModel):
    # id: Optional[UUID] = uuid4()
    name: str
    lastName: str
    phone: str
    email: str
    # roles: List[Role]


class TicketSelection(BaseModel):
    eventName: str
    category: str
    row: int
    seatNumber: int
    price: int
    # promoCode: Optional[str]
    buyer: Buyer


class TicketSelectionRequest(BaseModel):
    ticketSelections: List[TicketSelection]


class EventCreate(BaseModel):
    name: str
    description: str
    date: datetime
    venue: str


class Event(EventCreate):
    id: int

    class Config:
        orm_mode = True


class TestInput(BaseModel):
    test_string: str