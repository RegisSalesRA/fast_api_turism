from typing import List 
from pydantic import BaseModel
from app.infrastructure.api.schemas.point_turism.responses.point_turism_detail import PointTurismDetailResponse

class PointTurismListResponse(BaseModel):
    points: List[PointTurismDetailResponse]
