from pydantic import BaseModel 
from enum import Enum
from datetime import datetime 
from typing import Optional


class StatusChoice(str, Enum):
    PROCESSING = "Processing"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"


class CartOrder(BaseModel):
    user_id: int 
    price: float 
    paid_status: bool 
    order_date: Optional[datetime] = None 
    product_status: StatusChoice

    class Config:
        orm_mode = True  


class CartOrderItem(BaseModel):
    order_id: int 
    invoice_no: str # số hóa đơn 
    product_status: str 
    item: str 
    image: bytes 
    qty: int 
    price: float 
    total: float 

