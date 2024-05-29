# app/crud.py
from datetime import datetime

from sqlalchemy.orm import Session
from uuid import uuid4
from app.models import User, Consumer, Event, Ticket, TicketCategory, Hall, City
from app.schemas import User as UserSchema, Consumer as ConsumerSchema, Event as EventSchema, Ticket as TicketSchema, \
    TicketCategories as TicketCategorySchema, Hall as HallSchema, City as CitySchema


# Utility function to generate unique IDs
def generate_id():
    return str(uuid4())


# Create User
def create_user(db: Session, user: UserSchema):
    db_user = User(
        id=generate_id(),
        username=user.username,
        full_name=user.full_name,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Read User
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


# Update User
def update_user(db: Session, user_id: int, user: UserSchema):
    db_user = get_user(db, user_id)
    if db_user:
        db_user.username = user.username
        db_user.full_name = user.full_name
        db_user.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(db_user)
    return db_user


# Delete User
def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user


# Create Consumer
def create_consumer(db: Session, consumer: ConsumerSchema, user_id: int):
    db_consumer = Consumer(
        id=generate_id(),
        user_id=user_id,
        username=consumer.username,
        full_name=consumer.full_name,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.add(db_consumer)
    db.commit()
    db.refresh(db_consumer)
    return db_consumer


# Read Consumer
def get_consumer(db: Session, consumer_id: int):
    return db.query(Consumer).filter(Consumer.id == consumer_id).first()


# Update Consumer
def update_consumer(db: Session, consumer_id: int, consumer: ConsumerSchema):
    db_consumer = get_consumer(db, consumer_id)
    if db_consumer:
        db_consumer.username = consumer.username
        db_consumer.full_name = consumer.full_name
        db_consumer.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(db_consumer)
    return db_consumer


# Delete Consumer
def delete_consumer(db: Session, consumer_id: int):
    db_consumer = get_consumer(db, consumer_id)
    if db_consumer:
        db.delete(db_consumer)
        db.commit()
    return db_consumer


# Create Event
def create_event(db: Session, event: EventSchema):
    db_event = Event(
        id=generate_id(),
        event_name=event.name,
        description=event.description,
        data=event.data
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


# Read Event
def get_event(db: Session, event_id: int):
    return db.query(Event).filter(Event.id == event_id).first()


# Update Event
def update_event(db: Session, event_id: int, event: EventSchema):
    db_event = get_event(db, event_id)
    if db_event:
        db_event.event_name = event.name
        db_event.description = event.description
        db_event.data = event.data
        db.commit()
        db.refresh(db_event)
    return db_event


# Delete Event
def delete_event(db: Session, event_id: int):
    db_event = get_event(db, event_id)
    if db_event:
        db.delete(db_event)
        db.commit()
    return db_event


# Create Ticket
def create_ticket(db: Session, ticket: TicketSchema):
    db_ticket = Ticket(
        id=generate_id(),
        price=ticket.price,
        ticket_category_id=ticket.ticket_category_id,
        ticket_name=ticket.ticket_name
    )
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket


# Read Ticket
def get_ticket(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()


# Update Ticket
def update_ticket(db: Session, ticket_id: int, ticket: TicketSchema):
    db_ticket = get_ticket(db, ticket_id)
    if db_ticket:
        db_ticket.price = ticket.price
        db_ticket.ticket_category_id = ticket.ticket_category_id
        db_ticket.ticket_name = ticket.ticket_name
        db.commit()
        db.refresh(db_ticket)
    return db_ticket


# Delete Ticket
def delete_ticket(db: Session, ticket_id: int):
    db_ticket = get_ticket(db, ticket_id)
    if db_ticket:
        db.delete(db_ticket)
        db.commit()
    return db_ticket


# Create Ticket Category
def create_ticket_category(db: Session, ticket_category: TicketCategorySchema):
    db_ticket_category = TicketCategory(
        id=generate_id(),
        name=ticket_category.name
    )
    db.add(db_ticket_category)
    db.commit()
    db.refresh(db_ticket_category)
    return db_ticket_category


# Read Ticket Category
def get_ticket_category(db: Session, ticket_category_id: int):
    return db.query(TicketCategory).filter(TicketCategory.id == ticket_category_id).first()


# Update Ticket Category
def update_ticket_category(db: Session, ticket_category_id: int, ticket_category: TicketCategorySchema):
    db_ticket_category = get_ticket_category(db, ticket_category_id)
    if db_ticket_category:
        db_ticket_category.name = ticket_category.name
        db.commit()
        db.refresh(db_ticket_category)
    return db_ticket_category


# Delete Ticket Category
def delete_ticket_category(db: Session, ticket_category_id: int):
    db_ticket_category = get_ticket_category(db, ticket_category_id)
    if db_ticket_category:
        db.delete(db_ticket_category)
        db.commit()
    return db_ticket_category


# Create Hall
def create_hall(db: Session, hall: HallSchema):
    db_hall = Hall(
        id=generate_id(),
        name=hall.name
    )
    db.add(db_hall)
    db.commit()
    db.refresh(db_hall)
    return db_hall


# Read Hall
def get_hall(db: Session, hall_id: int):
    return db.query(Hall).filter(Hall.id == hall_id).first()


# Update Hall
def update_hall(db: Session, hall_id: int, hall: HallSchema):
    db_hall = get_hall(db, hall_id)
    if db_hall:
        db_hall.name = hall.name
        db.commit()
        db.refresh(db_hall)
    return db_hall


# Delete Hall
def delete_hall(db: Session, hall_id: int):
    db_hall = get_hall(db, hall_id)
    if db_hall:
        db.delete(db_hall)
        db.commit()
    return db_hall


# Create City
def create_city(db: Session, city: CitySchema):
    db_city = City(
        id=generate_id(),
        name=city.name,
        state=city.state
    )
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city


# Read City
def get_city(db: Session, city_id: int):
    return db.query(City).filter(City.id == city_id).first()


# Update City
def update_city(db: Session, city_id: int, city: CitySchema):
    db_city = get_city(db, city_id)
    if db_city:
        db_city.name = city.name
        db_city.state = city.state
        db.commit()
        db.refresh(db_city)
    return db_city


# Delete City
def delete_city(db: Session, city_id: int):
    db_city = get_city(db, city_id)
    if db_city:
        db.delete(db_city)
        db.commit()
    return db_city
