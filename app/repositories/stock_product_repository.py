from typing import List

from sqlalchemy.orm import Session

from models.stock_product_model import StockProductBase, StockProductModel


class StockProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_stock_products(self):
        return self.db.query(StockProductModel).all()
