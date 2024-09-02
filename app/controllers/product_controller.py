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


@router.get('/all-products/')
async def get_all_products(product_service: ProductService = Depends(get_product_service)):
    products = product_service.get_all_products()
    return products

@router.put('/edit-product/{product_id}')
async def update_product(product_id: int, new_product: ProductBase, product_service: ProductService = Depends(get_product_service)):
    try:
        product = product_service.update_product(product_id, new_product)
        return product
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

