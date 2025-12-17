from dataclasses import dataclass
from typing import Optional


@dataclass
class CategoryEntity:
    id: Optional[int]
    name: str
