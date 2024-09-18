from sqlalchemy.orm import Session

from models.card_model import CardModel

from schemas.schemas import CardBase


class CardRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_card(self, card_id: int):
        card = self.db.query(CardModel).filter(CardModel.id == card_id).first()
        return card

    def get_all_cards(self):
        cards = self.db.query(CardModel).all()
        return cards

    def create_card(self, card: CardModel):
        db_card = CardModel(number=card.number,
                            flag=card.flag)
        self.db.add(db_card)
        self.db.commit()
        self.db.refresh(db_card)
        return db_card

    def delete_card(self, card_id: int):
        db_card = self.get_card(card_id)
        self.db.delete(db_card)
        self.db.commit()
        return db_card

    def update_card(self, card_id: int, new_card: CardBase):
        db_card = self.get_card(card_id)
        db_card.number = new_card.number or db_card.number
        db_card.flag = new_card.flag or db_card.flag
        self.db.commit()
        self.db.refresh(db_card)
        return db_card
