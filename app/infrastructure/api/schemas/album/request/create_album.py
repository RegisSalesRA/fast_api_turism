from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List


class CreateAlbumRequest(BaseModel):
    title: Optional[str] = Field(None, max_length=255, description="Título do álbum")
    description: Optional[str] = Field(None, max_length=1000, description="Descrição do álbum")
    image_urls: Optional[List[HttpUrl]] = Field(None, description="Lista de URLs das imagens do álbum")
