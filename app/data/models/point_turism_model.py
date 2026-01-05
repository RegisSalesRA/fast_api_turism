from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from app.core.base import Base
from app.data.models.category_model import CategoryModel
from app.data.models.city_model import CityModel

class PointTurismModel(Base):
    __tablename__ = "point_turisms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String, nullable=True)
    review = Column(Float, default=0.0)
    image_id = Column(Integer, ForeignKey("images.id"), nullable=True)
    album_id = Column(Integer, ForeignKey("albums.id"), nullable=True)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=True)
    city_id = Column(Integer, ForeignKey("cities.id"), nullable=True)

    category = relationship("CategoryModel", backref="point_turisms")
    city = relationship("CityModel", backref="point_turisms")
    image = relationship("ImageModel", backref="point_turisms", foreign_keys=[image_id])
    album = relationship("AlbumModel", backref="point_turisms", foreign_keys=[album_id])

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
