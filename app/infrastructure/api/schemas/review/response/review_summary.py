from pydantic import BaseModel, ConfigDict


class ReviewSummaryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: str
    point_turism_id: int
    rating: float
