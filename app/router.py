from fastapi import APIRouter

from controllers.product_controller import router as product
from controllers.stock_product_controller import router as stock

from controllers.stock_product_controller import router as stock
api_router = APIRouter()

api_router.include_router(product, prefix='/product', tags=['product'])
api_router.include_router(stock, prefix='/stock', tags=['stock'])
