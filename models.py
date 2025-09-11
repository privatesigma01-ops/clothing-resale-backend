from pydantic import BaseModel
from typing import Optional

class ClothingItem(BaseModel):
    title: str
    description: Optional[str]
    original_price: float
    resale_price: float
    image_url: Optional[str]
    category: str
    size: Optional[str]
    condition: Optional[str]
    seller_name: Optional[str]
    tax_slab: Optional[float]
    delivery_charge: Optional[float]
    status: Optional[str] = "Pending"
