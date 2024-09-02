from fastapi import HTTPException
from repositories.product_repository import ProductRepository
from  models.product_model import ProductBase


class ProductService():
    def __init__(self, product_repository:ProductRepository):
        self.product_repository = product_repository
    
    def get_product(self, product_id: int):
        product = self.product_repository.get_product(product_id)
        if not product:
            raise HTTPException(status_code=404, detail='Product is not found')
        return product
    
    def get_all_products(self):
        try:
            return self.product_repository.get_all_products()
        except Exception as e:
            return {"message": "Something went wrong", "error": str(e)}
        
    
    def create_product(self, product_base: ProductBase):
        try:
            new_product = self.product_repository.create_product(product=product_base)
            return {"message": "Product added successfully", "product": new_product}
        except Exception as e:
            return {"message": "Something went wrong, the product was not added", "error": str(e)}
            
    def update_product(self, product_id: int, new_product: ProductBase):
        product = self.product_repository.update_product(product_id, new_product)
        if not product:
            raise HTTPException(status_code=404, detail='Product not found')
        return product