from fastapi import APIRouter
from controllers.product_controller import router as product
from controllers.stock_product_controller import router as stock_product
from controllers.trolley_controller import router as trolley
from controllers.payment_controller import router as payment
from controllers.card_controller import router as card

api_router = APIRouter()
api_router.include_router(product, prefix="/product", tags=["product"])
api_router.include_router(stock_product, prefix="/stock_product", tags=["stock_product"])
api_router.include_router(trolley, prefix="/trolley", tags=["trolley"])
api_router.include_router(payment, prefix="/payment", tags=["payment"])
api_router.include_router(card, prefix="/card", tags=["card"])
