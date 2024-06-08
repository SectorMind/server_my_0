# app/models.py

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, Float, Numeric
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    full_name = Column(String)
    email = Column(String)
    phone = Column(String)
    password = Column(String)
    role = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    consumer = relationship("Consumer", back_populates="user", uselist=False)


# TODO: связать username in User & username in Consumer
class Consumer(Base):
    __tablename__ = "consumer"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    username = Column(String, unique=True, index=True)
    full_name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user = relationship("User", back_populates="consumer")
    tickets = relationship("Ticket", secondary="consumer_ticket_link", back_populates="consumer")


# TODO: rename  Table to "PurchaseTable" with unic UUID
consumer_ticket_link = Table('consumer_ticket_link', Base.metadata,
                             Column('consumer_id', Integer, ForeignKey('consumer.id')),
                             Column('ticket_id', Integer, ForeignKey('ticket.id'))
                             )

event_ticket_link = Table('event_ticket_link', Base.metadata,
                          Column('event_id', Integer, ForeignKey('event.id')),
                          Column('ticket_id', Integer, ForeignKey('ticket.id'))
                          )


class Ticket(Base):
    __tablename__ = "ticket"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Numeric)
    ticket_category_id = Column(Integer, ForeignKey('ticket_category.id'))
    consumers = relationship("Consumer", secondary=consumer_ticket_link, back_populates="ticket")
    events = relationship("Event", secondary=event_ticket_link, back_populates="ticket")


event_hall_link = Table('event_hall_link', Base.metadata,
                        Column('event_id', Integer, ForeignKey('event.id'), primary_key=True),
                        Column('hall_id', Integer, ForeignKey('hall.id'), primary_key=True)
                        )


class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True, index=True)
    event_name = Column(String)
    description = Column(String)
    data = Column(String)
    tickets = relationship("Ticket", secondary=event_ticket_link, back_populates="event")
    halls = relationship("Hall", secondary=event_hall_link, back_populates="event")


ticket_category_link = Table('ticket_category_link', Base.metadata,
                             Column('ticket_id', Integer, ForeignKey('ticket.id')),
                             Column('ticket_category_id', Integer, ForeignKey('ticket_category.id'))
                             )

hall_city_link = Table('hall_city_link', Base.metadata,
                       Column('hall_id', Integer, ForeignKey('hall.id'), primary_key=True),
                       Column('city_id', Integer, ForeignKey('city.id'), primary_key=True)
                       )


class TicketCategory(Base):
    __tablename__ = "ticket_category"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    tickets = relationship("Ticket", secondary=ticket_category_link, back_populates="ticket_category")


class Hall(Base):
    __tablename__ = "hall"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    events = relationship("Event", secondary=event_hall_link, back_populates="hall")
    cities = relationship("City", secondary=hall_city_link, back_populates="hall")


class City(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    state = Column(String)
    halls = relationship("Hall", secondary=hall_city_link, back_populates="city")
