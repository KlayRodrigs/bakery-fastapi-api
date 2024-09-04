from sqlalchemy.orm import Session
from models.stock_product_model import StockProductBase, StockProductModel
from models.product_model import ProductModel
from core.settings import log

class StockProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_or_update_stock_product(self, stock_product: StockProductBase):
        try:
            product = self.db.query(ProductModel).filter(ProductModel.id == stock_product.product_id).first()
            if not product:
                raise ValueError("Product not found")

            existing_stock_product = self.db.query(StockProductModel).filter(StockProductModel.product_id == stock_product.product_id).first()
            if existing_stock_product:
                existing_stock_product.quantity += stock_product.quantity
                self.db.commit()
                self.db.refresh(existing_stock_product)
                return existing_stock_product
            else:
                db_stock_product = StockProductModel(quantity=stock_product.quantity, product_id=stock_product.product_id)
                self.db.add(db_stock_product)
                self.db.commit()
                self.db.refresh(db_stock_product)
                return db_stock_product
        except Exception as e:
            log.error(f"Error in create_or_update_stock_product: {str(e)}")
            self.db.rollback()
            raise

    def get_stock_product_by_id(self, stock_product_id: int):
        try:
            stock_product = self.db.query(StockProductModel).filter(StockProductModel.id == stock_product_id).first()
            return stock_product
        except Exception as e:
            log.error(f"Error in get_stock_product_by_id: {str(e)}")
            raise

    def get_all_stock_products(self):
        try:
            stock_products = self.db.query(StockProductModel).all()
            return stock_products
        except Exception as e:
            log.error(f"Error in get_all_stock_products: {str(e)}")
            raise