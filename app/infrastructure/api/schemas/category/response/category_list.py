from typing import List 
from pydantic import BaseModel
from app.infrastructure.api.schemas.category.response.category_detail import CategoryDetailResponse 


class CategoryListResponse(BaseModel):
    points: List[CategoryDetailResponse]
