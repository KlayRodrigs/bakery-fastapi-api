from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from models.payment_model import PaymentModel

from repositories.trolley_repository import TrolleyRepository

from repositories.stock_product_repository import StockProductRepository

from models.stock_product_model import StockProductModel
from models.trolley_model import TrolleyModel

from models.product_model import ProductModel



from models.trolley_model import trolley_items


class PaymentRepository:
    def __init__(self, db: Session):
        self.db = db
        self.trolley_repository = TrolleyRepository(db)
        self.stock_product_repository = StockProductRepository(db)

    def get_payment(self, payment_id: int):
        payment = self.db.query(PaymentModel).filter(PaymentModel.id == payment_id).first()
        return payment

    def get_all_payments(self):
        payments = self.db.query(PaymentModel).all()
        return payments

    def create_payment(self, payment: PaymentModel):
        global trolley_items
        db_payment = PaymentModel(trolley_id=payment.trolley_id,
                                  price=payment.price,
                                  type=payment.type,
                                  card_id=payment.card_id)
        self.db.add(db_payment)
        self.db.commit()
        self.db.refresh(db_payment)

        query = select(trolley_items).where(trolley_items.c.trolley_id == payment.trolley_id)
        trolley_items = self.db.execute(query).fetchall()

        for item in trolley_items:
            product_id = item[1]
            quantity = item[2]

            stock_product = self.db.query(StockProductModel).filter(StockProductModel.product_id == product_id).first()

            if stock_product:
                stock_product.quantity -= quantity
                self.db.add(stock_product)

            self.db.commit()
        return db_payment
