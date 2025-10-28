from pydantic import BaseModel, Field
from typing import Optional

class UpdatePointTurismRequest(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=255)
    image: Optional[str] = Field(None, description="URL da imagem")
    description: Optional[str] = Field(None, max_length=500) 
    category_id: Optional[int]
    review: Optional[float] = Field(None, ge=1, le=5, description="Média de avaliação (0–5)")
