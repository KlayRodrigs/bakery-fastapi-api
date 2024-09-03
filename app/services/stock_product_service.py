from models.stock_product_model import StockProductBase
from repositories.stock_product_repository import StockProductRepository


class StockProductService:
    def __init__(self, stock_product_repository: StockProductRepository):
        self.stock_product_repository = stock_product_repository

    def create_stock_product(self, stock_product_base: StockProductBase):
        try:
            new_stock_product = self.stock_product_repository.create_stock_product(stock_product=stock_product_base)
            return {"message": "Product added to Stock successfully", "stock_product": new_stock_product}
        except Exception as e:
            return {"message": "Somthing went wrong, the product was not added to stock", "error": str(e)}
