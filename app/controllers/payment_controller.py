from http.client import HTTPException

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from core.database import get_db
from repositories.payment_repository import PaymentRepository
from services.payment_service import PaymentService

from schemas.schemas import PaymentBase

from controllers.trolley_controller import get_trolley_service
from controllers.card_controller import get_card_service


def get_payment_service(db: Session = Depends(get_db)) -> PaymentService:
    payment_repository = PaymentRepository(db)
    trolley_service = get_trolley_service(db)
    card_service = get_card_service(db)
    return PaymentService(payment_repository, trolley_service, card_service)


router = APIRouter()


@router.post('/add/')
async def create_payment(payment_base: PaymentBase, payment_service: PaymentService = Depends(get_payment_service)):
    try:
        response = payment_service.create_payment(payment_base)
        return response
    except HTTPException as e:
        return e


@router.get('/get-payment/{payment_id}')
async def get_payment(payment_id: int, payment_service: PaymentService = Depends(get_payment_service)):
    try:
        response = payment_service.get_payment(payment_id)
        return response
    except HTTPException as e:
        return e


@router.get('/get-all-payments')
async def get_all_payments(payment_service: PaymentService = Depends(get_payment_service)):
    try:
        response = payment_service.get_all_payments()
        return response
    except HTTPException as e:
        return e
