# Router for ticket-related endpoints

# app/routers/tickets.py

"""
In this code:

    We define two endpoints using FastAPI's APIRouter: one for creating ticket selections (/ticket-selections/) and one for retrieving all ticket selections (/ticket-selections/).
    The create_ticket_selection endpoint expects a JSON payload conforming to the TicketSelection schema and creates a new ticket selection record in the database.
    The get_ticket_selections endpoint retrieves all ticket selections from the database.

These endpoints use the crud functions to interact with the database and return responses based on the specified Pydantic schemas.

Now, with the router defined, we can mount it in the main FastAPI application in the main.py file.
"""

from typing import List  # Import the List type

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

# Define test data for debugging purposes
test_data = {
    "eventName": "Concert",
    "category": "VIP",
    "row": 10,
    "seatNumber": 20,
    "price": 100,
    "buyer": {
        "name": "John",
        "lastName": "Doe",
        "phone": "123456789",
        "email": "john@example.com"
    }
}


@router.post("/ticket-selections/", response_model=schemas.TicketSelection)
def create_ticket_selection(ticket_selection: schemas.TicketSelection, db: Session = Depends(get_db)):
    db_ticket_selection = crud.create_ticket_selection(db, ticket_selection)
    return db_ticket_selection


@router.get("/ticket-selections/", response_model=List[schemas.TicketSelection])
def get_ticket_selections(db: Session = Depends(get_db)):
    return crud.get_ticket_selections(db)
