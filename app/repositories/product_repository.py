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