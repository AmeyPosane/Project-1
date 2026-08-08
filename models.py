from pydantic import BaseModel

class Plant(BaseModel):
    name: str
    price: int
    quantity: int
    