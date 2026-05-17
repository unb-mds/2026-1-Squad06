
#Conexão com o banco de dados

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./guardaia.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Dependência do FastAPI — abre e fecha a sessão do banco automaticamente."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()