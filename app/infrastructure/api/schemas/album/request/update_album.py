from pydantic import BaseModel, Field
from typing import Optional


class UpdateAlbumRequest(BaseModel):
    point_turism_id: Optional[int] = Field(None, description="ID do ponto turístico")
