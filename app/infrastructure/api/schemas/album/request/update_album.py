from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List


class UpdateAlbumRequest(BaseModel):
    point_turism_id: Optional[int] = Field(None, description="ID do ponto turístico")
    image_urls: Optional[List[HttpUrl]] = Field(None, max_length=10, description="Lista de URLs das imagens")
