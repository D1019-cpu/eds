from pydantic import BaseModel 


class Address(BaseModel):
    user_id: int 
    address: str 
    status: bool 
