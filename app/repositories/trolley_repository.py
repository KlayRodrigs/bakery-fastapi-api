from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.trolley_model import TrolleyModel

from models.product_model import ProductModel

from repositories.product_repository import ProductRepository

from models.trolley_model import trolley_items

from schemas.schemas import TrolleyBase

from models.stock_product_model import StockProductModel


class TrolleyRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_trolley(self, trolley_id: int):
        trolley = self.db.query(TrolleyModel).filter(TrolleyModel.id == trolley_id).first()
        return trolley

    def get_all_trolleys(self):
        trolleys = self.db.query(TrolleyModel).all()
        return trolleys

    def create_trolley(self, trolley: TrolleyBase):
        db_trolley = TrolleyModel(total_price=0.0)
        self.db.add(db_trolley)
        self.db.commit()
        self.db.refresh(db_trolley)

        total_price = 0.0

        for item in trolley.products:
            stock_product = self.db.query(StockProductModel).filter(StockProductModel.product_id == item.product_id).first()
            if not stock_product:
                raise HTTPException(status_code=404, detail=f"Product with ID {item.product_id} not found in stock")

            if stock_product.quantity < item.quantity:
                raise HTTPException(status_code=400,
                                    detail=f"Insufficient stock for product with ID {item.product_id}")

            if stock_product:
                self.db.execute(
                    trolley_items.insert().values(
                        trolley_id=db_trolley.id,
                        product_id=item.product_id,
                        quantity=item.quantity
                    )
                )
                product = self.db.query(ProductModel).filter(ProductModel.id == item.product_id).first()
                total_price += product.product_price * item.quantity

        db_trolley.total_price = total_price
        self.db.commit()
        return db_trolley

    def delete_trolley(self, trolley_id: int):
        db_trolley = self.get_trolley(trolley_id)
        self.db.delete(db_trolley)
        self.db.commit()
        return db_trolley

    # def update_trolley(self, trolley_id: int, product_id: int, new_trolley: TrolleyBase):
    #     db_trolley = self.get_trolley(trolley_id)
    #     db_trolley.product_id = ProductRepository.get_product(product_id=product_id)
    #
    #     db_trolley.quantity = new_trolley.quantity or db_trolley.quantity
    #     db_trolley.total_price = new_trolley.total_price or db_trolley.total_price
    #     self.db.commit()
    #     self.db.refresh(db_trolley)
    #     return db_trolley
