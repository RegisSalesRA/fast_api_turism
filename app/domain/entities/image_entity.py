from dataclasses import dataclass
from typing import Optional
from enum import Enum


@dataclass
class ImageEntity:
    id: Optional[int]
    url: str
    album_id: Optional[int] = None
    point_turism_id: Optional[int] = None

