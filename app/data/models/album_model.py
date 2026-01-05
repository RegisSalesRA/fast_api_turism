from sqlalchemy import Column, Integer, String, DateTime, func, Table, ForeignKey
from app.core.base import Base

# Tabela de associação para relacionamento muitos-para-muitos entre Album e Image
album_image_association = Table(
    'album_images',
    Base.metadata,
    Column('album_id', Integer, ForeignKey('albums.id'), primary_key=True),
    Column('image_id', Integer, ForeignKey('images.id'), primary_key=True)
)


class AlbumModel(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(1000), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
