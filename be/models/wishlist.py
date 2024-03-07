from pydantic import BaseModel 
from datetime import datetime
from typing import Optional


class Wishlist(BaseModel):
    user_id: int 
    product_id: int 
    date: Optional[datetime] = None # datetime 
