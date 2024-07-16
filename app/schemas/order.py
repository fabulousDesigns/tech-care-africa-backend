from datetime import datetime

from pydantic import BaseModel


class OrderBase(BaseModel):
    item: str
    amount: float
    customer_id: int

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    time: datetime

    class Config:
        orm_mode = True