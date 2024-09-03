from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db

from repositories.stock_product_repository import StockProductRepository
from services.stock_product_service import StockProductService

from models.stock_product_model import StockProductBase

router = APIRouter()


def get_stock_product_service(db: Session = Depends(get_db)) -> StockProductService:
    stock_product_repository = StockProductRepository(db)
    return StockProductService(stock_product_repository=stock_product_repository)


@router.put('/edit_stock_product/{stock_product_id}')
async def update_stock_product(stock_product_id: int, new_stock_product: StockProductBase, stock_product_service: StockProductService = Depends(get_stock_product_service)):
    try:
        stock_product = stock_product_service.update_stock_product(stock_product_id, new_stock_product)
        return stock_product
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
