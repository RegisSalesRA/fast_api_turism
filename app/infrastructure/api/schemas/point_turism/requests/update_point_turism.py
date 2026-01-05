from pydantic import BaseModel, Field
from typing import Optional
from app.domain.entities.point_turism_entity import PointTurismEntity

class UpdatePointTurismRequest(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=255)
    description: Optional[str] = Field(None, max_length=500)
    image: Optional[int] = Field(None, description="ID da imagem")
    album: Optional[int] = Field(None, description="ID do álbum")
    category_id: Optional[int] = Field(None, description="ID da categoria")
    city_id: Optional[int] = Field(None, description="ID da cidade")
    review: Optional[float] = Field(None, ge=0, le=5, description="Avaliação (0-5)")

    def to_entity(self, point_id: int) -> PointTurismEntity:
        return PointTurismEntity(
            id=point_id,
            name=self.name,
            description=self.description,
            image=self.image,
            album=self.album,
            category_id=self.category_id,
            city_id=self.city_id,
            review=self.review
        )
