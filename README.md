# Sale Order API

This project demonstrates a structured FastAPI application for managing sale orders, and their associated order lines using PostgreSQL.

## Project Structure

```
app/
├── api/               # API route definitions
├── crud/              # CRUD operations for database
├── db/                # Database connection setup
├── models/            # SQLAlchemy models
├── schemas/           # Pydantic schemas
├── main.py            # our FAST Api entry point
```

## Features

- Create sale orders with nested sale order lines
- Retrieve sale orders filtered by company_id or customer_id
- Organized modular structure for scalability and clarity

## Technology Stack

- Python 
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic

## API Endpoints

- `POST /sale_order/` – Create a sale order along with its order lines
- `GET /sale_order/` – Retrieve sale orders by company_id or customer_id

## Setup Instructions

1. Clone the repository
2. Create a venv and install dependencies
3. Configure the PostgreSQL database in `app/db/database.py`
4. Run the application using the command:
   ```
   uvicorn app.main:app --reload
   ```
5. Access the documentation at  `/redoc`
