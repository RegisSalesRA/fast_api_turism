from pydantic import BaseModel, Field, HttpUrl
from typing import List


class AlbumCreateSchema(BaseModel):
    point_turism_id: int = Field(..., description="ID do ponto turístico")
    image_urls: List[HttpUrl] = Field(..., max_length=10, description="Lista de URLs das imagens (máximo 10)")