from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from core.settings import settings, log
from typing import Generator

engine = create_engine(settings.URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    try:
        Base.metadata.create_all(bind=engine)
        log.debug(message="Tabela criada")
    except Exception as e:
        log.error(message=f"Erro ao criar tabelas: {e}")

# Base.metadata.create_all(bind=engine)
