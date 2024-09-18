from sqlalchemy.orm import Session

from models.product_model import ProductModel

from schemas.schemas import ProductBase


class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_product(self, product_id: int):
        product = self.db.query(ProductModel).filter(product_id == ProductModel.id).first()
        return product

    def get_all_products(self):
        products = self.db.query(ProductModel).all()
        return products

    def create_product(self, product: ProductBase):
        db_product = ProductModel(product_name=product.product_name,
                                  product_price=product.product_price)
        self.db.add(db_product)
        self.db.commit()
        return db_product

    def delete_product(self, product_id: int):
        db_product = self.get_product(product_id)
        self.db.delete(db_product)
        self.db.commit()
        return db_product

    def update_product(self, product_id: int, new_product: ProductBase):
        db_product = self.get_product(product_id)
        db_product.product_name = new_product.product_name or db_product.product_nam
        db_product.product_price = new_product.product_price or db_product.product_price
        self.db.commit()
        self.db.refresh(db_product)
        return db_product
