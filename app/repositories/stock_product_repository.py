from sqlalchemy.orm import Session
from models.stock_product_model import StockProductBase, StockProductModel
from models.product_model import ProductModel
from core.settings import log

class StockProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_or_update_stock_product(self, stock_product: StockProductBase):
        try:
            log.info(f"Checking if product with ID {stock_product.product_id} exists")
            product = self.db.query(ProductModel).filter(ProductModel.id == stock_product.product_id).first()
            if not product:
                raise ValueError("Product not found")

            log.info(f"Checking if stock product with product ID {stock_product.product_id} exists")
            existing_stock_product = self.db.query(StockProductModel).filter(StockProductModel.product_id == stock_product.product_id).first()
            if existing_stock_product:
                log.info(f"Updating quantity for stock product with product ID {stock_product.product_id}")
                existing_stock_product.quantity += stock_product.quantity
                self.db.commit()
                self.db.refresh(existing_stock_product)
                return existing_stock_product
            else:
                log.info(f"Creating new stock product with product ID {stock_product.product_id}")
                db_stock_product = StockProductModel(quantity=stock_product.quantity, product_id=stock_product.product_id)
                self.db.add(db_stock_product)
                self.db.commit()
                self.db.refresh(db_stock_product)
                return db_stock_product
        except Exception as e:
            log.error(f"Error in create_or_update_stock_product: {str(e)}")
            self.db.rollback()
            raise