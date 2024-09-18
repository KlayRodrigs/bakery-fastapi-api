from fastapi import HTTPException


from repositories.stock_product_repository import StockProductRepository
from services.product_service import ProductService

from schemas.schemas import StockProductBase


class StockProductService:
    def __init__(self, stock_products_repository: StockProductRepository, product_service: ProductService):
        self.stock_products_repository = stock_products_repository
        self.product_service = product_service

    def get_stock_product(self, stock_product_id: int):
        try:
            stock_product = self.stock_products_repository.get_stock_product(stock_product_id)
            if not stock_product:
                raise HTTPException(status_code=404, detail=f"Stock product with ID {stock_product_id} not found")
            return stock_product
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'Internal server error: {str(e)}')

    def get_all_stock_products(self):
        try:
            stock_products = self.stock_products_repository.get_all_stock_products()
            if not stock_products:
                raise HTTPException(status_code=404, detail=f"No stock products found")
            return stock_products
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'Internal server error: {str(e)}')

    def create_stock_product(self, stock_product_base: StockProductBase):
        self.product_service.get_product(product_id=stock_product_base.product_id)
        try:
            new_stock_product = self.stock_products_repository.create_stock_product(stock_product_base)
            return {'message': f'Stock Product created successfully'}
        except ValueError as e:
            return HTTPException(status_code=400, detail=f'Invalid data {str(e)}')
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'Internal server error: {str(e)}')

    def delete_stock_product(self, stock_product_id: int):
        self.get_stock_product(stock_product_id=stock_product_id)
        try:
            stock_product = self.stock_products_repository.delete_stock_product(stock_product_id)
            return {'message': f'Stock Product {stock_product_id} deleted successfully'}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'Internal server error: {str(e)}')

    def update_stock_product(self, stock_product_id: int, stock_product_base: StockProductBase):
        self.get_stock_product(stock_product_id=stock_product_id)
        try:
            stock_product = self.stock_products_repository.update_stock_product(stock_product_id, stock_product_base)
            return {'message': f'Stock Product {stock_product_id} updated successfully'}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'Internal server error: {str(e)}')
