from pydantic import BaseModel

class CategoryResponse(BaseModel):
    city_name: str
    total_points: int
    average_review: float
