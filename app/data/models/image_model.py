from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from app.core.base import Base


class ImageModel(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(500), nullable=False)
    point_turism_id = Column(Integer, ForeignKey("point_turisms.id"), nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
