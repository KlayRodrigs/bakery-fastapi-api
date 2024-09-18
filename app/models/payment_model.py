from core.database import Base
from sqlalchemy import Column, Integer, Float, ForeignKey, String
from sqlalchemy.orm import relationship


class PaymentModel(Base):
    __tablename__ = 'payment'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    price = Column(Float)
    type = Column(String)
    trolley_id = Column(Integer, ForeignKey('trolley.id'))
    card_id = Column(Integer, ForeignKey('card.id'))

    trolley = relationship("TrolleyModel", back_populates="payment")
    card = relationship("CardModel", back_populates="payment")
