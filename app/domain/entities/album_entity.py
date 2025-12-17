from dataclasses import dataclass
from typing import List


@dataclass
class AlbumEntity:
    id: Optional[int]
    title: str
    images: List[ImageEntity]
