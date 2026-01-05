from pydantic import BaseModel, Field, HttpUrl
from typing import Optional


class UpdateImageRequest(BaseModel):
    url: Optional[HttpUrl] = Field(None, description="URL da imagem")
