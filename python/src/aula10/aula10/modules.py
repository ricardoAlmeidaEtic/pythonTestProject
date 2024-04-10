from pydantic import BaseModel

class Product(BaseModel):
    name: str
    sku: int
    price: float
    enabled: bool
    id: int