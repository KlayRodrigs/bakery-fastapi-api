from fastapi import HTTPException

from repositories.payment_repository import PaymentRepository
from schemas.schemas import PaymentBase

from services.trolley_service import TrolleyService

from services.card_service import CardService


class PaymentService:
    def __init__(self, payment_repository: PaymentRepository, trolley_service: TrolleyService, card_service: CardService):
        self.payment_repository = payment_repository
        self.trolley_service = trolley_service
        self.card_service = card_service

    def get_payment(self, payment_id: int):
        try:
            payment = self.payment_repository.get_payment(payment_id)
            if not payment:
                raise HTTPException(status_code=404, detail=f'Payment with ID {payment_id} not found')
            return payment
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'Internal server error: {str(e)}')

    def get_all_payments(self):
        try:
            payments = self.payment_repository.get_all_payments()
            if not payments:
                raise HTTPException(status_code=404, detail=f'No Payments found')
            return payments
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'Internal server error: {str(e)}')

    def create_payment(self, payment_base: PaymentBase):
        self.trolley_service.get_trolley(trolley_id=payment_base.trolley_id)
        self.card_service.get_card(card_id=payment_base.card_id)
        try:
            new_payment = self.payment_repository.create_payment(payment_base)
            return {'message': f'Payment done successfully'}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'Internal server error: {str(e)}')
