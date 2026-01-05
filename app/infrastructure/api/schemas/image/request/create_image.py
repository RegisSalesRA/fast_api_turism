from pydantic import BaseModel, Field, HttpUrl


class CreateImageRequest(BaseModel):
    url: HttpUrl = Field(..., description="URL da imagem")
