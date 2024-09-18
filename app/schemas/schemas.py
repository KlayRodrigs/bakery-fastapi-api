from typing import List

from pydantic import BaseModel


class ProductBase(BaseModel):
    id: int
    product_name: str
    product_price: float

    class Config:
        orm_mode = True


class StockProductBase(BaseModel):
    product_id: int
    quantity: int

    class Config:
        orm_mode = True


class TrolleyBase(BaseModel):
    trolley_id: int
    total_price: float

    class Config:
        orm_mode = True


class PaymentBase(BaseModel):
    trolley_id: int
    price: float
    type: str
    card_id: int

    class Config:
        orm_mode = True


class CardBase(BaseModel):
    number: str
    flag: str

    class Config:
        orm_mode = True


class CardOut(CardBase):
    payments: List[PaymentBase]


class PaymentOut(PaymentBase):
    cards: List[CardBase]


class ProductOut(ProductBase):
    trolleys: List[TrolleyBase]


class TrolleyOut(TrolleyBase):
    products: List[StockProductBase]

