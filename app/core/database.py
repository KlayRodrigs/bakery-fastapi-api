from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import Depends
from sqlalchemy.ext.declarative import declarative_base
from core.settings import settings
from sqlalchemy.orm import Session 
from typing import Annotated


engine = create_engine(settings.URL_DATABASE)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind=engine)

Base = declarative_base()   
    
def get_db(db):    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]