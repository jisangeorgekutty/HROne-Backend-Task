from fastapi import FastAPI
from routes import products, orders

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the HROne Backend API"}
app.include_router(products.router)
app.include_router(orders.router)

