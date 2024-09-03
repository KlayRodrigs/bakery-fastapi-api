from fastapi import HTTPException
from models.stock_product_model import StockProductBase
from repositories.stock_product_repository import StockProductRepository


class StockProductService:
    def __init__(self, stock_product_repository: StockProductRepository):
        self.stock_product_repository = stock_product_repository

    def update_stock_product(self, stock_product_id: int, new_product: StockProductBase):
        stock_product = self.stock_product_repository.update_stock_product(stock_product_id, new_product)
        if not stock_product:
            raise HTTPException(status_code=404, detail='Stock product not found')
        return stock_product
