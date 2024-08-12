from fastapi import APIRouter, Depends, HTTPException, status
from requests import Session
from repositories.product_repository import ProductRepository
from services.product_service import ProductService
from core.database import get_db
from models.product_model import ProductBase

router = APIRouter()

def get_product_service(db: Session = Depends(get_db)) -> ProductService:
    product_repository = ProductRepository(db)
    return ProductService(product_repository=product_repository)

                
@router.post('/add/')
async def create_product(product_base: ProductBase, product_service: ProductService = Depends(get_product_service)):
    response = product_service.create_product(product_base)
    if "error" in response:
        raise HTTPException(status_code=500, detail=response["message"])
    return response
        
@router.get('/{product_id}')
async def get_product(product_id: int, product_service: ProductService = Depends(get_product_service)):
    product = product_service.get_product(product_id)
    return product