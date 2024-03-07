from pydantic import BaseModel
from datetime import datetime 
from typing import Optional


class Vendor(BaseModel):
    # id auto generated 
    vendor_id: str # uuid
    name: str 
    image: bytes 
    description: str 
    user_id: int 
    address: str 
    contact: str 
    date: Optional[datetime] = None # datetime 
    