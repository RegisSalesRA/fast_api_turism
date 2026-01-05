from pydantic import BaseModel, ConfigDict
from typing import List


class AlbumDetailResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str | None
    description: str | None
