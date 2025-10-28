from dataclasses import dataclass
from typing import Optional

@dataclass
class PointTurismEntity:
    id: Optional[int]
    name: str
    image: str
    description: Optional[str]
    city_id: int
    category_id: int
    review: float = 0.0
