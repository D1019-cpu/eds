from pydantic import BaseModel 
from enum import Enum


class UserType(str, Enum):
    ADMIN = "admin"
    CUSTOMER = "customer"


class UserLoginForm(BaseModel):
    # id: int 
    email: str 
    password: str 

class User(BaseModel):
    # id: int 
    username: str 
    email: str 
    password: str 
    user_type: UserType 

    class Config:
        orm_mode = True 

