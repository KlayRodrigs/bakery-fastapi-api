from models.card_model import CardModel
from sqlalchemy import Column, Integer, ForeignKey


class CreditModel(CardModel):
    __tablename__ = 'credit'

    id = Column(Integer, ForeignKey('card.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'credit',
    }
