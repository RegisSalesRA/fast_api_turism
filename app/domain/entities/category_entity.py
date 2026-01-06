from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class CategoryEntity:
    id: Optional[int]
    name: str
    created_at: datetime = datetime.utcnow()
