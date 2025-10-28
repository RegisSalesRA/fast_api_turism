from pydantic import BaseModel
from typing import Optional

class FilterPointTurismRequest(BaseModel):
    name: Optional[str] = None 
    category_id: Optional[int] = None
    min_review: Optional[float] = None
