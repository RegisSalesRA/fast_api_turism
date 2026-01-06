from pydantic import BaseModel, ConfigDict
from typing import Optional, List


class AlbumDetailResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    point_turism_id: Optional[int]
    image_urls: Optional[List[str]] = None
