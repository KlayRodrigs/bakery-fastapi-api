from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.database import get_db
from services.card_service import CardService

from repositories.card_repository import CardRepository

from schemas.schemas import CardBase

router = APIRouter()


def get_card_service(db: Session = Depends(get_db)) -> CardService:
    card_repository = CardRepository(db)
    return CardService(card_repository)


@router.post('/add/')
async def add_card(card_base: CardBase, card_service: CardService = Depends(get_card_service)):
    try:
        response = card_service.create_card(card_base)
        return response
    except HTTPException as e:
        raise e


@router.get('/get-card/{card_id}')
def get_card(card_id: int, card_service: CardService = Depends(get_card_service)):
    try:
        response = card_service.get_card(card_id)
        return response
    except HTTPException as e:
        raise e


@router.get('/get-all-cards')
async def get_all_cards(card_service: CardService = Depends(get_card_service)):
    try:
        response = card_service.get_all_cards()
        return response
    except HTTPException as e:
        raise e


@router.put('/edit-card/{card_id}')
async def update_card(card_id: int, card_base: CardBase, card_service: CardService = Depends(get_card_service)):
    try:
        response = card_service.update_card(card_id, card_base)
        return response
    except HTTPException as e:
        raise e


@router.delete('/delete-card/{card_id}')
async def delete_card(card_id: int, card_service: CardService = Depends(get_card_service)):
    try:
        response = card_service.delete_card(card_id)
        return response
    except HTTPException as e:
        raise e
