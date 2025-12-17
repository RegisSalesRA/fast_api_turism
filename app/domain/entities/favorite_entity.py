from dataclasses import dataclass
from datetime import datetime


@dataclass
class FavoriteEntity:
    user_id: str
    point_turism_id: int
    created_at: datetime = datetime.utcnow()
