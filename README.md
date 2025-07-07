# 🛒 E-commerce Backend API with FastAPI

This project is a **RESTful E-commerce backend API** built using **FastAPI** and **SQLAlchemy**. It manages Users, Products, and Orders, and can be integrated with a frontend interface for a full-stack e-commerce solution.

---

## 🚀 Features

- ✅ User registration and authentication
- 🛍️ Product creation, listing, and stock management
- 📦 Order creation with total price calculation
- 📡 Fast and asynchronous API with FastAPI
- 🛠️ SQLite/MySQL compatible (configured via SQLAlchemy)
- 📚 Well-structured modular codebase

---

## 📁 Project Structure

ecommerce_fastapi/
│
├── app/
│ ├── main.py # FastAPI entry point
│ ├── models.py # SQLAlchemy models (User, Product, Order)
│ ├── schemas.py # Pydantic schemas for request/response validation
│ ├── crud.py # All database operations
│ ├── database.py # DB connection setup
│ └── routers/ # Optional: to split routes (modular)
│
├── create_tables.py # Create all tables from models
├── requirements.txt # Required Python packages
└── README.md # Project documentation


---

## 🧑‍💻 Tech Stack

- **Backend Framework:** FastAPI
- **ORM:** SQLAlchemy
- **Database:** SQLite (default) / MySQL
- **Validation:** Pydantic
- **Tooling:** Uvicorn for ASGI server

---

## 🧪 API Endpoints Overview

| Method | Endpoint          | Description               |
|--------|-------------------|---------------------------|
| POST   | /users/           | Register a new user       |
| GET    | /users/           | List all users            |
| POST   | /products/        | Add a new product         |
| GET    | /products/        | Get all products          |
| POST   | /orders/          | Create a new order        |
| GET    | /orders/          | View all orders           |

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Amanj-0349/E-COMMERCE_FASTAPI/tree/my-new-branch
cd ecommerce-fastapi
```

python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

pip install -r requirements.txt

python create_tables.py

uvicorn app.main:app --reload

The API will be available at: http://127.0.0.1:8000

Visit the interactive docs at: http://127.0.0.1:8000/docs
