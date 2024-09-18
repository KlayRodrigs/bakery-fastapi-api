from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.database import get_db

from repositories.product_repository import ProductRepository
from services.product_service import ProductService

from schemas.schemas import ProductBase

router = APIRouter()


def get_product_service(db: Session = Depends(get_db)) -> ProductService:
    product_repository = ProductRepository(db)
    return ProductService(product_repository)


@router.post('/add/')
async def create_product(product_base: ProductBase, product_service: ProductService = Depends(get_product_service)):
    try:
        response = product_service.create_product(product_base)
        return response
    except HTTPException as e:
        raise e


@router.get('/get-product/{product_id}')
async def get_product(product_id: int, product_service: ProductService = Depends(get_product_service)):
    try:
        response = product_service.get_product(product_id)
        return response
    except HTTPException as e:
        raise e


@router.get('/get-all-products')
async def get_all_products(product_service: ProductService = Depends(get_product_service)):
    try:
        response = product_service.get_all_products()
        return response
    except HTTPException as e:
        raise e


@router.put('/edit-product/{product_id}')
async def update_product(product_id: int, product_base: ProductBase, product_service: ProductService = Depends(get_product_service)):
    try:
        response = product_service.update_product(product_id, product_base)
        return response
    except HTTPException as e:
        raise e


@router.delete('/delete-product/{product_id}')
async def delete_product(product_id: int, product_service: ProductService = Depends(get_product_service)):
    try:
        response = product_service.delete_product(product_id)
        return response
    except HTTPException as e:
        raise e
