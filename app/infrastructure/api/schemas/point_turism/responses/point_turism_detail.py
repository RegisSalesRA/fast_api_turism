from pydantic import BaseModel

class PointTurismDetailResponse(BaseModel):
    id: int
    name: str
    image: str
    description: str | None
    city_id: int
    category_id: int
    review: float

    class Config:
        orm_mode = True  # permite converter diretamente de modelos SQLAlchemy
