from dataclasses import dataclass
from typing import Optional
from enum import Enum

class ImageType(Enum):
    COVER = "cover"
    GALLERY = "gallery"

@dataclass
class ImageEntity:
    id: Optional[int]
    url: str
    type: ImageType = ImageType.GALLERY
