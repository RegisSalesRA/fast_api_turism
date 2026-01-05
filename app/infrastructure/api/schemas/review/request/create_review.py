from pydantic import BaseModel, Field
from typing import Optional


class CreateReviewRequest(BaseModel):
    user_id: str = Field(..., description="ID do usuário")
    point_turism_id: int = Field(..., description="ID do ponto turístico")
    rating: float = Field(..., ge=0, le=5, description="Classificação de 0 a 5")
    comment: Optional[str] = Field(None, max_length=1000, description="Comentário da revisão")
