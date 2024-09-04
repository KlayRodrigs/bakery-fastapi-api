from fastapi import HTTPException
from core.settings import log
from models.stock_product_model import StockProductBase
from repositories.stock_product_repository import StockProductRepository

class StockProductService:
    def __init__(self, stock_product_repository: StockProductRepository):
        self.stock_product_repository = stock_product_repository

    def get_stock_product_by_id(self, stock_product_id: int):
        try:
            log.info(f"Fetching stock product with ID {stock_product_id}")
            stock_product = self.stock_product_repository.get_stock_product_by_id(stock_product_id)
            if not stock_product:
                log.warning(f"Stock product with ID {stock_product_id} not found")
                raise HTTPException(status_code=404, detail="Stock product not found")
            log.info(f"Stock product found: {stock_product}")
            return stock_product
        except HTTPException as he:
            log.error(f"HTTP error in get_stock_product_by_id: {str(he)}")
            raise
        except Exception as e:
            log.error(f"Error in get_stock_product_by_id: {str(e)}")
            raise

    def create_stock_product(self, stock_product_base: StockProductBase):
        try:
            log.info(f"Creating or updating stock product with data: {stock_product_base}")
            updated_stock_product = self.stock_product_repository.create_or_update_stock_product(stock_product=stock_product_base)
            log.info(f"Stock product created or updated successfully: {updated_stock_product}")
            return {"message": "Product added to Stock successfully", "stock_product": updated_stock_product}
        except ValueError as ve:
            log.error(f"Validation error: {str(ve)}")
            return {"message": str(ve), "error": "validation_error"}
        except Exception as e:
            log.error(f"Error creating or updating stock product: {str(e)}")
            return {"message": "Something went wrong, the product was not added to stock", "error": str(e)}
    
    def get_all_stock_products(self):
        try:
            log.info("Fetching all stock products")
            stock_products = self.stock_product_repository.get_all_stock_products()
            if not stock_products:
                log.warning("No stock products found")
                raise HTTPException(status_code=404, detail="No stock products found")
            log.info(f"Found {len(stock_products)} stock products")
            return stock_products
        except HTTPException as he:
            log.error(f"HTTP error in get_all_stock_products: {str(he)}")
            raise
        except Exception as e:
            log.error(f"Error in get_all_stock_products: {str(e)}")
            raise