from pydantic import BaseModel, ConfigDict
from datetime import datetime


class ReviewDetailResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: str
    point_turism_id: int
    rating: float
    comment: str | None
    created_at: datetime
