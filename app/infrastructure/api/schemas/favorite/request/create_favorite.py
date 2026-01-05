from pydantic import BaseModel, Field


class CreateFavoriteRequest(BaseModel):
    user_id: str = Field(..., description="ID do usuário")
    point_turism_id: int = Field(..., description="ID do ponto turístico")
