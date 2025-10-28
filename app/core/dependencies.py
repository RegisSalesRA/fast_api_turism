from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def get_db():
    """
    Cria uma sessão do SQLAlchemy para usar nas rotas.
    Uso em FastAPI: Depends(get_db)
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
