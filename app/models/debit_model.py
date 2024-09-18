from models.card_model import CardModel
from sqlalchemy import Column, Integer, ForeignKey


class DebitModel(CardModel):
    __tablename__ = 'debit'

    id = Column(Integer, ForeignKey('card.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'debit',
    }
