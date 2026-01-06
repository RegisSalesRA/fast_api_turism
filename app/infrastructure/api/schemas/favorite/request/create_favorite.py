from pydantic import BaseModel, Field


class CreateFavoriteRequest(BaseModel):
    point_turism_id: int = Field(..., description="ID do ponto turístico")
