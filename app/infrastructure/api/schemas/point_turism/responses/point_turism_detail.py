from pydantic import BaseModel, ConfigDict

class PointTurismDetailResponse(BaseModel):
    id: int
    name: str
    images: str           
    description: str | None
    category_id: int | None
    city_id: int | None
    review: float        
