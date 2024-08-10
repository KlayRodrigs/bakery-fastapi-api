from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Annotated
from sqlalchemy.ext.declarative import declarative_base
from settings import settings
from fastapi import Depends
from sqlalchemy.orm import Session

class DataBase():
    base = declarative_base()
    def get_db():
        engine = create_engine(settings.URL_DATABASE)
        SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind=engine)
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

dataBase = DataBase()
db_dependency = Annotated[Session, Depends(dataBase.get_db())]