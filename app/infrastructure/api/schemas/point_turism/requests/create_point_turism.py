from pydantic import BaseModel, Field
from typing import Optional

class CreatePointTurismRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=255)
    image: str = Field(..., description="URL da imagem do ponto turístico")
    description: Optional[str] = Field(None, max_length=500)
    city_id: int
    category_id: int
