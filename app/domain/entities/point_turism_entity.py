from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime


@dataclass
class PointTurismEntity:
    id: Optional[int]
    name: str
    description: Optional[str]
    category_id: Optional[int]
    city_id: Optional[int]
    review: float = 0.0
    created_at: datetime = datetime.utcnow()
