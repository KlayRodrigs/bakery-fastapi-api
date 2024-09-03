from sqlalchemy.orm import Session

from models.stock_product_model import StockProductBase, StockProductModel


class StockProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def update_stock_product(self, stock_product_id: int, new_product: StockProductBase):
        try:
            # get_stock_product
            db_stock_product = self.db.query(StockProductModel).filter(StockProductModel.id == stock_product_id).first()
            if not db_stock_product:
                raise Exception('Stock product not found')

            db_stock_product.quantity = new_product.quantity or db_stock_product.quantity
            self.db.commit()
            self.db.refresh(db_stock_product)
            return db_stock_product

        except Exception as e:
            self.db.rollback()
            raise Exception(f'Error updating product: {str(e)}')
