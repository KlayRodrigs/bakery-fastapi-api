from requests import Session
from  models.product_model import ProductBase, ProductModel

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_product(self, product_id: int):
        return self.db.query(ProductModel).filter(ProductModel.id == product_id).first()
    
    def create_product(self, product: ProductBase):
        db_product = ProductModel(product_name=product.product_name)
        self.db.add(db_product)
        self.db.commit()
        return db_product
    
    def update_product(self, product_id: int, new_product: ProductBase):
        try:
            db_product = self.get_product(product_id)
            if not db_product:
                raise Exception(f"Product with ID {product_id} not found")

            db_product.product_name = new_product.product_name or db_product.product_name
            self.db.commit()
            self.db.refresh(db_product)
            return db_product
        
        except Exception as e:
            self.db.rollback()
            raise Exception(f"Error updating product: {str(e)}")