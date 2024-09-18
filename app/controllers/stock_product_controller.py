from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.database import get_db

from repositories.stock_product_repository import StockProductRepository
from services.stock_product_service import StockProductService

from controllers.product_controller import get_product_service

from schemas.schemas import StockProductBase

router = APIRouter()


def get_stock_product_service(db: Session = Depends(get_db)) -> StockProductService:
    stock_product_repository = StockProductRepository(db)
    product_service = get_product_service(db)
    return StockProductService(stock_product_repository, product_service)


@router.post('/add/')
async def create_stock_product(stock_product_base: StockProductBase, stock_product_service: StockProductService = Depends(get_stock_product_service)):
    try:
        response = stock_product_service.create_stock_product(stock_product_base)
        return response
    except HTTPException as e:
        raise e


@router.get('/get-stock-product/{stock_product_id}')
async def get_stock_product(stock_product_id: int, stock_product_service: StockProductService = Depends(get_stock_product_service)):
    try:
        response = stock_product_service.get_stock_product(stock_product_id)
        return response
    except HTTPException as e:
        raise e


@router.get('/get-all-stock_product')
async def get_all_stock_products(stock_product_service: StockProductService = Depends(get_stock_product_service)):
    try:
        response = stock_product_service.get_all_stock_products()
        return response
    except HTTPException as e:
        raise e


@router.put('/edit-stock-product/{stock_product_id}')
async def update_stock_product(stock_product_id: int, stock_product_base: StockProductBase, stock_product_service: StockProductService = Depends(get_stock_product_service)):
    try:
        response = stock_product_service.update_stock_product(stock_product_id, stock_product_base)
        return response
    except HTTPException as e:
        raise e


@router.delete('/delete-stock-product/{stock_product_id}')
async def delete_stock_product(stock_product_id: int, stock_product_service: StockProductService = Depends(get_stock_product_service)):
    try:
        response = stock_product_service.delete_stock_product(stock_product_id)
        return response
    except HTTPException as e:
        raise e
