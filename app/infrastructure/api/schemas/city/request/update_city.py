from pydantic import BaseModel, Field

class UpdateCityRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=255, description="Nome da cidade")
    state: str = Field(..., min_length=1, max_length=100, description="Estado")
    country: str = Field(default="Brasil", max_length=100, description="País")
    description: str | None = Field(None, description="Descrição da cidade")

