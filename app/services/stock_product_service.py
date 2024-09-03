from typing import List
from fastapi import HTTPException
from models.stock_product_model import StockProductBase
from repositories.stock_product_repository import StockProductRepository


class StockProductService:
    def __init__(self, stock_product_repository: StockProductRepository):
        self.stock_product_repository = stock_product_repository

    def get_all_stock_products(self):
        stock_products = self.stock_product_repository.get_all_stock_products()
        if stock_products is None:
            raise HTTPException(status_code=404, detail="No stock products found")
        return stock_products
