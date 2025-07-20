from fastapi import APIRouter,HTTPException
from models.schema import Order, OrderResponse
from bson import ObjectId
from db.mongo import db


router = APIRouter()

@router.post("/orders", status_code=201, response_model=OrderResponse)
async def create_order(order: Order):
    for item in order.items:
        try:
            product = await db.products.find_one({"_id": ObjectId(item.productId)})
        except Exception:
            raise HTTPException(status_code=400, detail=f"Invalid productId: {item.productId}")
        
        if not product:
            raise HTTPException(status_code=404, detail=f"Product not found: {item.productId}")
    order = order.dict()
    res = await db.orders.insert_one(order)
    return {"id": str(res.inserted_id)}

@router.get("/orders/{user_id}", status_code=200)
async def get_orders(user_id: str, limit: int = 10, offset: int = 0):
    cursor  = db.orders.find({"userId": user_id}).skip(offset).limit(limit)

    orders = []
    async for order in cursor:
        items = []
        total_price = 0.0

        for item in order["items"]:
            try:
                product = await db.products.find_one({"_id": ObjectId(item["productId"])})
            except Exception:
                product = None

            product_info = {
                "productDetails": {
                    "id": item["productId"],
                    "name": product["name"] if product else "Unknown"
                },
                "qty": item["qty"]
            }

            # Total price calculate
            if product:
                total_price += item["qty"] * product["price"]

            items.append(product_info)

        orders.append({
            "id": str(order["_id"]),
            "items": items,
            "total": round(total_price, 2)
        })

    return {
        "data": orders,
        "page": {
            "next": offset + limit,
            "limit": offset,
            "previous": offset - limit
        }
    }