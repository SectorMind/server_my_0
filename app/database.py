# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, decl_api, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from .config import DATABASE_URL

# Create SQLAlchemy engine
# TODO: add echo_pool for useful logging
engine = create_engine(DATABASE_URL, echo=True)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base: decl_api.DeclarativeMeta = declarative_base()


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


if __name__ == '__main__':
    from sqlalchemy import MetaData
    metadata = MetaData()
    metadata.reflect(bind=engine)
    metadata.drop_all(bind=engine)

    metadata.create_all(bind=engine)
