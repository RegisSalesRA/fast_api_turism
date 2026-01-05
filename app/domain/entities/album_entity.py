from dataclasses import dataclass
from typing import List, Optional

from app.domain.entities.image_entity import ImageEntity


@dataclass
class AlbumEntity:
    id: Optional[int]
    title: str
    images: List[ImageEntity]
