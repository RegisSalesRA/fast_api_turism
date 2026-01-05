from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class ReviewEntity:
    id: Optional[int]
    user_id: str
    point_turism_id: int
    rating: float
    comment: Optional[str] = None
    created_at: datetime = datetime.utcnow()
