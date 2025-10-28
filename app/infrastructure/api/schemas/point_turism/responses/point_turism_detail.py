from pydantic import BaseModel

class PointTurismDetailResponse(BaseModel):
    id: int
    name: str
    image: str
    description: str | None 
    category_id: int
    review: float

    class Config:
        orm_mode = True   