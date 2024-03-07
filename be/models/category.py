from pydantic import BaseModel 


class Category(BaseModel):
    category_id: str # uuidv4
    name: str 
    image: bytes 

