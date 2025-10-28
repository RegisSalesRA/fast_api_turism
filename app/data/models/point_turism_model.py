from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.core.dependencies import Base

class PointTurismModel(Base):
    __tablename__ = "point_turisms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    image = Column(String(255), nullable=False)
    description = Column(String, nullable=True)
    city_id = Column(Integer, ForeignKey("cities.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    review = Column(Float, default=0.0)

    city = relationship("CityModel", back_populates="points")
    category = relationship("CategoryModel", back_populates="points")
