from pydantic import BaseModel, ConfigDict

class PointTurismDetailResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    name: str
    description: str | None
    category_id: int | None
    city_id: int | None
    review: float        
