from fastapi import APIRouter, Depends, HTTPException
from database import db
from models import ClothingItem
from auth import get_current_user
from bson import ObjectId

router = APIRouter()

@router.post("/add")
async def add_item(item: ClothingItem, user: str = Depends(get_current_user)):
    item_dict = item.dict()
    item_dict["seller_name"] = user
    result = await db.items.insert_one(item_dict)
    return {"message": "Item added", "id": str(result.inserted_id)}

@router.get("/approved")
async def get_approved():
    items = []
    cursor = db.items.find({"status": "Approved"})
    async for document in cursor:
        document["_id"] = str(document["_id"])
        items.append(document)
    return items

@router.get("/pending")
async def get_pending(user: str = Depends(get_current_user)):
    items = []
    cursor = db.items.find({"status": "Pending"})
    async for document in cursor:
        document["_id"] = str(document["_id"])
        items.append(document)
    return items

@router.put("/approve/{item_id}")
async def approve_item(item_id: str, user: str = Depends(get_current_user)):
    result = await db.items.update_one({"_id": ObjectId(item_id)}, {"$set": {"status": "Approved"}})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item approved"}

@router.put("/reject/{item_id}")
async def reject_item(item_id: str, user: str = Depends(get_current_user)):
    result = await db.items.update_one({"_id": ObjectId(item_id)}, {"$set": {"status": "Rejected"}})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item rejected"}
