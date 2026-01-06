from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class ImageEntity:
    id: Optional[int]
    url: str
    point_turism_id: Optional[int] = None
    created_at: datetime = datetime.utcnow()

