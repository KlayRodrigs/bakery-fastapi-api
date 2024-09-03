from fastapi import HTTPException
from repositories.stock_product_repository import StockProductRepository


class StockProductService:
    def __init__(self, stock_product_repository: StockProductRepository):
        self.stock_product_repository = stock_product_repository

    def get_stock_product_by_id(self, stock_product_id: int):
        stock_product = self.stock_product_repository.get_stock_product_by_id(stock_product_id)
        if not stock_product:
            raise HTTPException(status_code=404, detail="Stock product not found")
        return stock_product
