from sqlalchemy.orm import Session

from models.stock_product_model import StockProductModel

from schemas.schemas import StockProductBase


#from repositories.product_repository import ProductRepository


class StockProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_stock_product(self, stock_product_id: int):
        stock_product = self.db.query(StockProductModel).filter(StockProductModel.id == stock_product_id).first()
        return stock_product

    def get_all_stock_products(self):
        stock_products = self.db.query(StockProductModel).all()
        return stock_products

    def create_stock_product(self, stock_product: StockProductBase):

        db_stock_product = StockProductModel(quantity=stock_product.quantity,
                                             product_id=stock_product.product_id)
        self.db.add(db_stock_product)
        self.db.commit()
        return db_stock_product

    def delete_stock_product(self, stock_product_id: int):
        db_stock_product = self.get_stock_product(stock_product_id)
        self.db.delete(db_stock_product)
        self.db.commit()
        return db_stock_product

    def update_stock_product(self, stock_product_id: int, new_stock_product: StockProductBase):
        db_stock_product = self.get_stock_product(stock_product_id)
        db_stock_product.quantity = new_stock_product.quantity or db_stock_product.quantity
        db_stock_product.product_id = new_stock_product.product_id or db_stock_product.product_id
        self.db.commit()
        self.db.refresh(db_stock_product)
        return db_stock_product
