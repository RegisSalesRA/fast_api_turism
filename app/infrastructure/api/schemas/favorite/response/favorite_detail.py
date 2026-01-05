from pydantic import BaseModel, ConfigDict
from datetime import datetime


class FavoriteDetailResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: str
    point_turism_id: int
    created_at: datetime
