from pydantic import BaseModel, Field
from typing import Optional


class UpdateAlbumRequest(BaseModel):
    title: Optional[str] = Field(None, max_length=255, description="Título do álbum")
    description: Optional[str] = Field(None, max_length=1000, description="Descrição do álbum")
