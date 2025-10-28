from pydantic import BaseModel
from typing import Optional

class FilterPointTurismRequest(BaseModel):
    name: Optional[str] = None
    city_id: Optional[int] = None
    category_id: Optional[int] = None
    min_review: Optional[float] = None
