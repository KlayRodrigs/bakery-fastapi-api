from sqlalchemy.orm import Session

from models.stock_product_model import StockProductBase, StockProductModel


class StockProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_stock_product_by_id(self, stock_product_id: int):
        return self.db.query(StockProductModel).filter(StockProductModel.id == stock_product_id).first()
