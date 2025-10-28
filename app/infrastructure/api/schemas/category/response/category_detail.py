from pydantic import BaseModel

class CategoryDetailResponse(BaseModel):
    id: int
    name: str 