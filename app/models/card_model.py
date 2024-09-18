from core.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class CardModel(Base):
    __tablename__ = 'card'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    number = Column(String(20))
    flag = Column(String, index=True)

    payment = relationship('PaymentModel', back_populates='card')

    # __mapper_args__ = {
    #     'polymorphic_identity': 'card',
    #     'polymorphic_on': id
    # }


