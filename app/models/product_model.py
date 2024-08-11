from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, func
from core.database import Base

class ProductModel(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key = True, index = True)
    product_name = Column(String, index = True)
    created_at = Column(DateTime,index = True, server_default=func.now())

class ProductBase(BaseModel):
    product_name: str