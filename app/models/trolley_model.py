from typing import List, TYPE_CHECKING

from core.database import Base
from fastapi.openapi.models import Schema
from pydantic import BaseModel
from sqlalchemy import Column, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship


trolley_items = Table(
    'trolley_items', Base.metadata,
    Column('trolley_id', Integer, ForeignKey('trolley.id'), primary_key=True),
    Column('product_id', Integer, ForeignKey('products.id'), primary_key=True),
    Column('quantity', Integer)
)


class TrolleyModel(Base):
    __tablename__ = 'trolley'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    total_price = Column(Float, index=True)

    products = relationship('ProductModel', secondary=trolley_items, back_populates='trolleys')
    payment = relationship('PaymentModel', back_populates='trolley')


