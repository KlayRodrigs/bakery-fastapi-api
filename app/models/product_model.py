from typing import Optional, List

from pydantic import BaseModel
from sqlalchemy import Column, String, Integer, Float
from core.database import Base
from sqlalchemy.orm import relationship


from models.trolley_model import trolley_items


class ProductModel(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_name = Column(String, index=True, unique=True)
    product_price = Column(Float, index=True)

    stock = relationship('StockProductModel', back_populates='product')
    trolleys = relationship('TrolleyModel', secondary=trolley_items, back_populates='products')




