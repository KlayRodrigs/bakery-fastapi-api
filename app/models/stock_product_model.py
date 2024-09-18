from typing import List

from pydantic import BaseModel
from sqlalchemy import Column, Integer, ForeignKey
from core.database import Base
from sqlalchemy.orm import relationship


class StockProductModel(Base):
    __tablename__ = 'stock_products'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    quantity = Column(Integer, index=True)

    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship('ProductModel', back_populates='stock')
    #trolley = relationship('TrolleyModel', back_populates='products')


