from sqlalchemy import Column, Integer, String, Float, DateTime, func
from app.core.base import Base

class PointTurismModel(Base):
    __tablename__ = "point_turisms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    image = Column(String(255), nullable=False)
    description = Column(String, nullable=True) 
    review = Column(Float, default=0.0)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
