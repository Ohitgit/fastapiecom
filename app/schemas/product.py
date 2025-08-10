from pydantic import BaseModel
from typing import Optional
from .category import CategoryRead

class ProductBase(BaseModel):
    name: str
    price: float
    category_id: int

class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    id: int
    category: CategoryRead

    class Config:
        orm_mode = True
