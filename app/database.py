# Database connection setup
"""
This code does the following:

    Defines the database URL. You can obtain this URL from your PostgreSQL database provider or set it as an environment variable for security.
    Creates a SQLAlchemy engine using the database URL.
    Creates a session factory using sessionmaker.
    Defines a base class for declarative models.
    Defines a get_db() function that yields a new database session for each request. This function will be used with FastAPI's dependency injection system to provide a database session to your route functions.

Once you've set up the database.py file, you can move on to defining the SQLAlchemy models in the models.py file.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import os

# Database URL
DATABASE_URL = os.getenv("DATABASE_URL")  # Update with your actual database URL

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()


# Function to get a new database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    except SQLAlchemyError as e:
        db.rollback()
        raise
    finally:
        db.close()
