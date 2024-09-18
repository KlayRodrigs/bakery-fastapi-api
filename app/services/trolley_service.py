from fastapi import HTTPException


from repositories.trolley_repository import TrolleyRepository

from schemas.schemas import TrolleyBase

from services.stock_product_service import StockProductService


class TrolleyService:
    def __init__(self, trolley_repository: TrolleyRepository, stock_product_service: StockProductService):
        self.trolley_repository = trolley_repository
        self.stock_product_service = stock_product_service

    def get_trolley(self, trolley_id: int):
        try:
            trolley = self.trolley_repository.get_trolley(trolley_id)
            if not trolley:
                raise HTTPException(status_code=404, detail="Trolley not found")
            return trolley
        except Exception as e:
            raise HTTPException(status_code=404, detail=f'Internal server error: {str(e)}')

    def get_all_trolleys(self):
        try:
            trolleys = self.trolley_repository.get_all_trolleys()
            if not trolleys:
                raise HTTPException(status_code=404, detail='Trolley not found')
            return trolleys
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'Internal serve error: {str(e)}')

    def create_trolley(self, trolley_base: TrolleyBase):
        try:
            trolley = self.trolley_repository.create_trolley(trolley_base)
            return {'message:' f'Trolley created'}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'Internal server error: {str(e)}')

    def delete_trolley(self, trolley_id: int):
        self.get_trolley(trolley_id)
        try:
            trolley = self.trolley_repository.delete_trolley(trolley_id)
            return {'message:' f'Trolley {trolley_id} deleted'}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'Internal server error: {str(e)}')

    def update_trolley(self, trolley_id: int, trolley_base: TrolleyBase):
        try:
            trolley = self.trolley_repository.delete_trolley(trolley_id)
            return {'message:' f'Trolley {trolley_id} updated'}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'Internal server error: {str(e)}')
