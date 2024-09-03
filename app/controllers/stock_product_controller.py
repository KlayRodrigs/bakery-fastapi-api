from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db

from repositories.stock_product_repository import StockProductRepository
from services.stock_product_service import StockProductService


router = APIRouter()


def get_stock_product_service(db: Session = Depends(get_db)) -> StockProductService:
    stock_product_repository = StockProductRepository(db)
    return StockProductService(stock_product_repository=stock_product_repository)


@router.get('/{stock_products_id}')
async def get_stock_product_by_id(stock_product_id: int, stock_product_service: StockProductService = Depends(get_stock_product_service)):
    stock_product = stock_product_service.get_stock_product_by_id(stock_product_id)
    return stock_product
