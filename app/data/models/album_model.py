from sqlalchemy import Column, Integer, String, DateTime, func, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.core.base import Base
from sqlalchemy.dialects.postgresql import ARRAY
class AlbumModel(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True, index=True)

    point_turism_id = Column(Integer, ForeignKey("point_turisms.id"), nullable=False)

    # até 10 links
    image_urls = Column(ARRAY(String), nullable=False, default=list)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    point_turism = relationship("PointTurismModel", backref="albums")