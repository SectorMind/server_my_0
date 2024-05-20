# app/routers/users.py

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()


@router.post("/users/", response_model=schemas.User)
def create_user(users: schemas.User, db: Session = Depends(get_db)):
    db_users = crud.create_user(db, users)
    return db_users


@router.get("/users/", response_model=List[schemas.User])
def read_users(db: Session = Depends(get_db)):
    users = crud.get_user(db)
    return users


@router.post("/event/", response_model=schemas.Event)
def create_user(events: schemas.Event, db: Session = Depends(get_db)):
    db_events = crud.create_event(db, events)
    return db_events


@router.get("/event/", response_model=List[schemas.Event])
def read_event(db: Session = Depends(get_db)):
    events = crud.get_event(db)
    return events
