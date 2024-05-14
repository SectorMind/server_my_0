# FastAPI application entry point
"""
In this code:

    We import the tickets router from app.routers.
    We create an instance of the FastAPI application (app).
    We create database tables by calling Base.metadata.create_all(bind=engine). This ensures that the database tables defined in the models are created when the application starts.
    We mount the tickets.router under the /api/v1 prefix. This means that endpoints defined in the tickets.py router will be accessible under the /api/v1 path.

With this setup, the main FastAPI application is configured to handle requests related to ticket selections.

Next, you can run the FastAPI application and test the ticket-related endpoints using tools like curl, Postman, or any HTTP client.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routers import tickets, events, users, my_test

import logging


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log',  # Log to a file
    filemode='a'  # Append mode
)

app = FastAPI()

# Allow requests from the origin of your frontend application
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",  # Add additional origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Mount routers
# app.include_router(tickets.router, prefix="/api/v1")

# Include the router
app.include_router(my_test.router, prefix="/api/v1")

# @app.get("/")
# def read_root():
#     try:
#         # Code that might raise an exception
#         raise Exception("An error occurred")
#     except Exception as e:
#         # Log the exception
#         logging.exception("An error occurred: %s", str(e))
#         # Allow the exception to propagate and be handled by FastAPI's default exception handlers
#         raise  # Re-raise the exception
