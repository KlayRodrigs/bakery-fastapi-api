from pydantic import BaseModel
from sqlalchemy import ForeignKey, Integer, Column
from core.database import Base


class StockProductModel(Base):
    __tablename__ = 'stock_products'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    quantity = Column(Integer, nullable=False, index=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)


class StockProductBase(BaseModel):
    quantity: int
    product_id: int
