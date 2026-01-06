from pydantic import BaseModel, Field, HttpUrl
from typing import Optional


class CreateImageRequest(BaseModel):
    url: HttpUrl = Field(..., description="URL da imagem")
    album_id: Optional[int] = Field(None, description="ID do álbum (se pertence a um álbum)")
    point_turism_id: Optional[int] = Field(None, description="ID do ponto turístico (se é capa do ponto)")
