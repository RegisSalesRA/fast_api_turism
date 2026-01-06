from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class CityEntity:
    id: Optional[int]
    name: str
    state: str
    country: str = "Brasil"
    description: Optional[str] = None
    review: float = 0.0
    created_at: datetime = datetime.utcnow()
