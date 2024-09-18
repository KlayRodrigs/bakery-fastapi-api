from fastapi import HTTPException


from repositories.product_repository import ProductRepository

from schemas.schemas import ProductBase


class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def get_product(self, product_id: int):
        try:
            product = self.product_repository.get_product(product_id)
            if not product:
                raise HTTPException(status_code=404, detail=f'Product with ID {product_id} not found')
            return product
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'Internal server error: {str(e)}')

    def get_all_products(self):
        try:
            products = self.product_repository.get_all_products()
            if not products:
                raise HTTPException(status_code=404, detail=f'No products found')
            return products
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'Internal server error: {str(e)}')

    def create_product(self, product_base: ProductBase):
        try:
            new_product = self.product_repository.create_product(product_base)
            return {'message': f'Product created successfully'}
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f'Invalid data: {str(e)}')
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'Internal server error: {str(e)}')

    def delete_product(self, product_id: int):
        self.get_product(product_id=product_id)
        try:
            product = self.product_repository.delete_product(product_id)
            return {'message': f'Product {product_id} deleted successfully'}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'Internal server error: {str(e)}')

    def update_product(self, product_id: int, product_base: ProductBase):
        self.get_product(product_id=product_id)
        try:
            product = self.product_repository.update_product(product_id, product_base)
            return {'message': f'Product {product_id} updated successfully'}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'Internal server error: {str(e)}')
