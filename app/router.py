from fastapi import APIRouter
from controllers.product_controller import router as product

api_router = APIRouter()
api_router.include_router(product, prefix='/product', tags=['product'],)
