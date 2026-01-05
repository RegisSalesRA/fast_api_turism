from pydantic import BaseModel, Field
from typing import Optional


class UpdateReviewRequest(BaseModel):
    rating: Optional[float] = Field(None, ge=0, le=5, description="Classificação de 0 a 5")
    comment: Optional[str] = Field(None, max_length=1000, description="Comentário da revisão")
