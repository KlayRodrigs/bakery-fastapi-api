from fastapi import HTTPException

from repositories.card_repository import CardRepository
from schemas.schemas import CardBase


class CardService:
    def __init__(self, card_repository: CardRepository):
        self.card_repository = card_repository

    def get_card(self, card_id: int):
        try:
            card = self.card_repository.get_card(card_id)
            if not card:
                raise HTTPException(status_code=404, detail="Card not found")
            return card
        except Exception as e:
            raise HTTPException(status_code=404, detail=f'Internal server error: {str(e)}')

    def get_all_cards(self):
        try:
            cards = self.card_repository.get_all_cards()
            if not cards:
                raise HTTPException(status_code=404, detail="Card not found")
            return cards
        except Exception as e:
            raise HTTPException(status_code=404, detail=f'Internal server error: {str(e)}')

    def create_card(self, card_base: CardBase):
        try:
            card = self.card_repository.create_card(card_base)
            return {'message:' f'Card saved'}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'Internal server error: {str(e)}')

    def delete_card(self, card_id: int):
        self.get_card(card_id=card_id)
        try:
            card = self.card_repository.delete_card(card_id)
            return {'message:' f'Card with ID {card_id} deleted successfully'}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'Internal server error: {str(e)}')

    def update_card(self, card_id: int, card_base: CardBase):
        self.get_card(card_id=card_id)
        try:
            card = self.card_repository.update_card(card_id, card_base)
            return {'message:' f'Card with ID {card_id} saved successfully'}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'Internal server error: {str(e)}')
