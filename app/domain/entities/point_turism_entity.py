from dataclasses import dataclass
from typing import Optional, List

from app.domain.entities.image_entity import ImageEntity


@dataclass
class PointTurismEntity:
    id: Optional[int]
    name: str
    description: Optional[str]
    category_id: Optional[int]
    city_id: Optional[int]
    image: Optional[int]
    album: List[ImageEntity]
    review: float = 0.0
