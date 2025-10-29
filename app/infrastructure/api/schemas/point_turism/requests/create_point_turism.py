from pydantic import BaseModel, Field
from typing import Optional

class CreatePointTurismRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=255)
    image: str = Field(..., description="URL da imagem do ponto turístico")
    description: Optional[str] = Field(None, max_length=500)
    category_id: Optional[int] = Field(None, description="ID da categoria")
    city_id: Optional[int] = Field(None, description="ID da cidade")
    review: Optional[float] = Field(0.0, ge=0, le=5, description="Avaliação (0-5)")
