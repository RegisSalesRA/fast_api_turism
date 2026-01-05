from dataclasses import dataclass
from typing import Optional
from enum import Enum


@dataclass
class ImageEntity:
    id: Optional[int]
    url: str

