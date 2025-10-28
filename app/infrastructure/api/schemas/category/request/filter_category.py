from pydantic import BaseModel
from typing import Optional

class FilterCategoryRequest(BaseModel):
    name: Optional[str] = None 