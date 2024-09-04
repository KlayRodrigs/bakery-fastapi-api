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

@router.post('/add/')
async def create_stock_product(stock_product_base: StockProductBase,
                                         stock_product_service: StockProductService = Depends(get_stock_product_service)):
    
    response = stock_product_service.create_stock_product(stock_product_base)
    if "error" in response:
        if response["error"] == "validation_error":
            raise HTTPException(status_code=400, detail=response['message'])
        raise HTTPException(status_code=500, detail=response['message'])
    return response

@router.get('/{stock_products_id}')
async def get_stock_product_by_id(stock_product_id: int, stock_product_service: StockProductService = Depends(get_stock_product_service)):
    stock_product = stock_product_service.get_stock_product_by_id(stock_product_id)
    return stock_product

@router.get('/list_products/')
async def get_all_stock_products(stock_product_service: StockProductService = Depends(get_stock_product_service)):
    stock_products = stock_product_service.get_all_stock_products()
    return stock_products
