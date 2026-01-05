from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func
from app.core.base import Base


class ReviewModel(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False)
    point_turism_id = Column(Integer, ForeignKey("point_turism.id"), nullable=False)
    rating = Column(Float, nullable=False)
    comment = Column(String(1000), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
