from fastapi import APIRouter, status
from core.database import db_dependency
import models
import models.product_model
from core.database import engine

router = APIRouter()

class ProductController:
    models.product_model.Base.metadata.create_all(bind=engine)  
    
    @router.post('/add/')
    async def create_product(db: db_dependency, product: models.product_model.ProductBase):
        db_product = models.product_model.ProductModel(product_name=product.product_name)
        db.add(db_product)
        db.commit()