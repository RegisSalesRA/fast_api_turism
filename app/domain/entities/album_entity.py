from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime


@dataclass
class AlbumEntity:
    id: Optional[int]
    point_turism_id: Optional[int] = None
    image_urls: Optional[List[str]] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
