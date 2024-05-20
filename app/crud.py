# app/crud.py

from sqlalchemy.orm import Session
from app import models, schemas
from sqlalchemy.exc import IntegrityError


def create_user(db: Session, user: schemas.User):
    try:
        db_user = models.User(
            username=user.username,
            full_name=user.full_name
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        db.rollback()
        existing_user = db.query(models.User).filter(models.User.username == user.username).first()
        if existing_user:
            existing_user.full_name = user.full_name
            db.commit()
            db.refresh(existing_user)
            return existing_user
        else:
            raise


def get_user(db: Session):
    return db.query(models.User).all()


def create_event(db: Session, event: schemas.User):
    db_event = models.Event(
        event_name=event.name,
        description=event.description,
        data=event.data
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def get_event(db: Session):
    return db.query(models.Event).all()
