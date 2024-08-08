from pydantic import BaseModel
from typing import List

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    email: str
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True