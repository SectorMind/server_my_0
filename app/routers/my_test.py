from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()


@router.post("/test/", response_model=schemas.TestInput)
def create_test_item(test_input: schemas.TestInput, db: Session = Depends(get_db)):
    return crud.create_test_string(db, test_input)


@router.get("/test/")
def get_test():
    # Add your logic here
    return {"message": "This is a test endpoint"}