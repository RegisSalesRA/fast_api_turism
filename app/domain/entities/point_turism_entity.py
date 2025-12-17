from dataclasses import dataclass
from typing import Optional, List


@dataclass
class PointTurismEntity:
    id: Optional[int]
    name: str
    description: Optional[str]
    category_id: Optional[int]
    city_id: Optional[int]
    images: List[ImageEntity]
    review: float = 0.0
