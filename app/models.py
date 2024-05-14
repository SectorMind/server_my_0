from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean  # Import the Boolean type
from sqlalchemy.orm import relationship
from app.database import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    date = Column(DateTime)
    venue = Column(String)

    # Relationship with tickets
    tickets = relationship("Ticket", back_populates="event")


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"))
    category = Column(String)
    row_number = Column(Integer)
    seat_number = Column(Integer)
    price = Column(Integer)
    available_quantity = Column(Integer)

    # Define relationship with Reservation
    reservations = relationship("Reservation", back_populates="ticket")

    # Relationship with event
    event = relationship("Event", back_populates="tickets")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    full_name = Column(String)
    email = Column(String)
    phone = Column(String)

    # Relationship with reservations
    reservations = relationship("Reservation", back_populates="user")


class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    ticket_id = Column(Integer, ForeignKey("tickets.id"))
    reserved_quantity = Column(Integer)
    reservation_time = Column(DateTime)
    payment_completed = Column(Boolean, default=False)

    # Define relationship with Ticket
    ticket = relationship("Ticket", back_populates="reservations")

    # Relationship with user
    user = relationship("User", back_populates="reservations")


class TicketSelection(Base):
    __tablename__ = "ticket_selections"

    id = Column(Integer, primary_key=True, index=True)
    eventName = Column(String, index=True)
    category = Column(String)
    row = Column(Integer)
    seatNumber = Column(Integer)
    price = Column(Integer)
    buyer_name = Column(String)
    buyer_lastName = Column(String)
    buyer_phone = Column(String)
    buyer_email = Column(String)


class TestModel(Base):
    __tablename__ = 'test_models'

    id = Column(Integer, primary_key=True, index=True)
    test_string = Column(String, index=True)