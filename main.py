from fastapi import FastAPI
from routes import products, orders  # ✅ this works fine for your structure

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the HROne Backend API!"}
app.include_router(products.router)
app.include_router(orders.router)

