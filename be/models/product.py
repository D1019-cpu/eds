from pydantic import BaseModel 
from enum import Enum
from datetime import datetime 
from typing import Optional


class Status(str, Enum):
    DRAFT = "Draft" 
    DISABLED = "Disabled"
    REJECTED = "Rejected"
    IN_REVIEW = "In Review"
    PUBLISHED = "Published"


class Rating(str, Enum):
    ONE = "★☆☆☆☆"
    TWO = "★★☆☆☆"
    THREE = "★★★☆☆"
    FOUR = "★★★★☆"
    FIVE = "★★★★★"


class Product(BaseModel):
    # id: primary key (auto generate)
    product_id: str # uuid
    user_id: int
    category_id: int 
    vendor_id: int 
    name: str 
    image: bytes  
    description: str 
    price: float 
    old_price: float 
    specifications: str # thông số kỹ thuật
    type: str 
    stock_count: int 
    life: Optional[datetime] = None # datetime 
    mfd: str # Manufactured
    product_status: Status 
    featured: bool 
    status: bool 
    digital: bool 
    sku: str 
    created_at: Optional[datetime] = None # time 
    updated_at: Optional[datetime] = None # time 


class ProductReview(BaseModel):
    user_id: int 
    product_id: int # primary key of Product 
    review: str 
    rating: Rating
    date: Optional[datetime] = None # time
