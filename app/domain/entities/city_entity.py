from dataclasses import dataclass
from typing import Optional


@dataclass
class CityEntity:
    id: Optional[int]
    name: str
    state: str
    country: str = "Brasil"
    description: Optional[str] = None
    review: float = 0.0
