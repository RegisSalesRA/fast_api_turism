from pydantic import BaseModel

class PointTurismSummaryResponse(BaseModel):
    city_name: str
    total_points: int
    average_review: float
