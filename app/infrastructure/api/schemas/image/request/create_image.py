from pydantic import BaseModel, Field, HttpUrl
from typing import Optional


class CreateImageRequest(BaseModel):
    url: HttpUrl = Field(..., description="URL da imagem")
    point_turism_id: Optional[int] = Field(None, description="ID do point turism")
