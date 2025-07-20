# 🛍️ HROne Backend Task – E-commerce API

A sample backend application built using **FastAPI** and **MongoDB**, simulating core functionalities of an e-commerce platform (like Flipkart or Amazon).

---

## 🚀 Live Demo

> 🌐 [Deployed Base URL](https://your-app.onrender.com)  
> ⚠️ Replace with your actual deployed URL (Render/Railway)

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

## ⚙️ Setup Instructions (Local)

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/hrone-backend-task.git
cd hrone-backend-task
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

### 3. Run Locally

```bash
uvicorn main:app --reload
```