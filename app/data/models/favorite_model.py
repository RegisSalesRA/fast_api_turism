from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, UniqueConstraint, func
from app.core.base import Base


class FavoriteModel(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False)
    point_turism_id = Column(Integer, ForeignKey("point_turism.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    __table_args__ = (UniqueConstraint('user_id', 'point_turism_id', name='uq_user_point_turism'),)
