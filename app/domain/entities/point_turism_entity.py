from dataclasses import dataclass
from typing import Optional

@dataclass
class PointTurismEntity:
    id: Optional[int]
    name: str
    image: str
    description: Optional[str]
    category_id: Optional[int] = None
    city_id: Optional[int] = None
    review: float = 0.0
