from sqlalchemy.orm import Session

from models.stock_product_model import StockProductBase, StockProductModel


class StockProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_stock_product(self, stock_product: StockProductBase):
        db_stock_product = StockProductModel(quantity=stock_product.quantity)
        self.db.add(db_stock_product)
        self.db.commit()
        return db_stock_product
