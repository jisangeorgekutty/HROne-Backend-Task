from fastapi import APIRouter, Query
from models.schema import Product, ProductResponse
from db.mongo import db
from typing import Optional

router = APIRouter()

@router.post("/products", status_code=201, response_model=ProductResponse)
async def create_product(product: Product):
    res = await db.products.insert_one(product.dict())
    return {"id": str(res.inserted_id)}

@router.get("/products", status_code=200)
async def list_products(name: Optional[str] = None,size: Optional[str] = None,limit: int = 10,offset: int = 0):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["sizes.size"] = size

    res = db.products.find(query).skip(offset).limit(limit)

    products = []
    async for product in res:
        products.append({
            "id": str(product["_id"]),
            "name": product["name"],
            "price": product["price"]
        })

    return {
        "data": products,
        "page": {
            "next": offset + limit,
            "limit": offset,
            "previous": offset - limit
        }
    }