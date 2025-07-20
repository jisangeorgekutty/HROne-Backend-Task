# 🛍️ HROne Backend Task – E-commerce API

A sample backend application built using **FastAPI** and **MongoDB**, simulating core functionalities of an e-commerce platform (like Flipkart or Amazon).

---

## 🚀 Live Demo

> 🌐 [Deployed Base URL](https://hrone-backend-qnnf.onrender.com)  

---

## 🧰 Tech Stack

- **FastAPI** – Modern async web framework for Python.
- **MongoDB Atlas (M0)** – NoSQL cloud database.
- **Motor** – Async MongoDB driver.
- **Uvicorn** – Lightning-fast ASGI server.

---

## 📂 Project Structure
```bash
HROne-Backend-Task/
├── db/
│ └── mongo.py # MongoDB connection using Motor
├── models/
│ └── schema.py # Pydantic request/response schemas
├── routes/
│ ├── products.py # Product APIs
│ └── orders.py # Order APIs
├── main.py # Entry point of the FastAPI app
├── .env # Environment variables (MongoDB URL)
├── .gitignore
├── requirements.txt
└── README.md
```

---

---

## 📬 API Endpoints

### 1. Create Product

- **Endpoint**: `POST /products`

- **Request**:
```json
{
  "name": "T-Shirt",
  "price": 399.0,
  "sizes": [
    {
      "size": "M",
      "quantity": 10
    }
  ]
}
```
- **Response**:
```json
{
  "id": "mongo_object_id"
}
```

### 2. List Products

- **Endpoint**: GET /products

- **Response**:
```json
{
  "data": [
    {
      "id": "product_id",
      "name": "T-Shirt",
      "price": 399.0
    }
  ],
  "page": {
    "next": 10,
    "limit": 0,
    "previous": -10
  }
}
```

### 3. Create Order

- **Endpoint**: POST /orders

- **Request**:
```json
{
  "userId": "user_1",
  "items": [
    {
      "productId": "mongo_object_id",
      "qty": 2
    }
  ]
}
```
- **Response**:
```json
{
  "id": "order_id"
}
```

### 4. Get User Orders

- **Endpoint**: GET /orders/{userId}

- **Response**:
```json
{
  "data": [
    {
      "id": "order_id",
      "items": [
        {
          "productDetails": {
            "id": "product_id",
            "name": "T-Shirt"
          },
          "qty": 2
        }
      ],
      "total": 798.0
    }
  ],
  "page": {
    "next": 10,
    "limit": 0,
    "previous": -10
  }
}
```

---

## ⚙️ Setup Instructions (Local)

### 1. Clone the Repo

```bash
git clone https://github.com/jisangeorgekutty/HROne-Backend-Task.git
cd HROne-Backend-Task
```

### 2. Install Dependencies

```bash
python -m venv env
source env/bin/Activate 
pip install -r requirements.txt
```

### 3. Add MongoDB URI

Create a .env file:

```bash
MONGO_URL=mongodb+srv://<username>:<password>@cluster0.mongodb.net/hrone?retryWrites=true&w=majority
```

### 4. Run Locally

```bash
uvicorn main:app --reload
```

---
