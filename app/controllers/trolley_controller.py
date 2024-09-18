from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.database import get_db

from services.trolley_service import TrolleyService


from repositories.trolley_repository import TrolleyRepository


from schemas.schemas import TrolleyOut, TrolleyBase

from controllers.stock_product_controller import get_stock_product_service

router = APIRouter()


def get_trolley_service(db: Session = Depends(get_db)) -> TrolleyService:
    trolley_repository = TrolleyRepository(db)
    stock_product_service = get_stock_product_service(db)
    return TrolleyService(trolley_repository, stock_product_service)


@router.post('/add/')
async def create_trolley(trolley_base: TrolleyOut, trolley_service: TrolleyService = Depends(get_trolley_service)):
    try:
        response = trolley_service.create_trolley(trolley_base)
        return response
    except HTTPException as e:
        raise e


@router.get('/get-trolley/{trolley_id}')
async def get_trolley(trolley_id: int, trolley_service: TrolleyService = Depends(get_trolley_service)):
    try:
        response = trolley_service.get_trolley(trolley_id)
        return response
    except HTTPException as e:
        raise e


@router.get('/get-all-trolleys')
async def get_all_trolleys(trolley_service: TrolleyService = Depends(get_trolley_service)):
    try:
        response = trolley_service.get_all_trolleys()
        return response
    except HTTPException as e:
        raise e


@router.put('/edit-trolley/{trolley_id}')
async def update_trolley(trolley_id: int, trolley_base: TrolleyBase, trolley_service: TrolleyService = Depends(get_trolley_service)):
    try:
        response = trolley_service.update_trolley(trolley_id, trolley_base)
        return response
    except HTTPException as e:
        raise e


@router.delete('/delete-trolley/{trolley_id}')
async def delete_trolley(trolley_id: int, trolley_service: TrolleyService = Depends(get_trolley_service)):
    try:
        response = trolley_service.delete_trolley(trolley_id)
        return response
    except HTTPException as e:
        raise e
