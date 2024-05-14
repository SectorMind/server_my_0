# CRUD operations for interacting with the database

"""
In this code:

    We define a create_ticket_selection function to create a new ticket selection record in the database based on the provided Pydantic schema.
    We define a get_ticket_selections function to retrieve all ticket selections from the database.

These are basic implementations of CRUD operations for ticket selections. Depending on your application requirements, you may need to add more functionality or refine these operations further.

Next, we'll continue by defining FastAPI routers in the routers/ directory to handle HTTP requests and integrate these CRUD operations.
"""

from sqlalchemy.orm import Session
from app import models, schemas

from app.models import TestModel
from app.schemas import TestInput


def create_ticket_selection(db: Session, ticket_selection: schemas.TicketSelection):
    db_ticket_selection = models.TicketSelection(
        eventName=ticket_selection.eventName,
        category=ticket_selection.category,
        row=ticket_selection.row,
        seatNumber=ticket_selection.seatNumber,
        price=ticket_selection.price,
        buyer_name=ticket_selection.buyer.name,
        buyer_lastName=ticket_selection.buyer.lastName,
        buyer_phone=ticket_selection.buyer.phone,
        buyer_email=ticket_selection.buyer.email
    )
    db.add(db_ticket_selection)
    db.commit()
    db.refresh(db_ticket_selection)
    return db_ticket_selection


def get_ticket_selections(db: Session):
    return db.query(models.TicketSelection).all()


def create_event(db: Session, event: schemas.EventCreate):
    db_event = models.Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def create_test_string(db: Session, test_input: TestInput):
    db_test = TestModel(test_string=test_input.test_string)
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test