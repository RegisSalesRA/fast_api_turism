from pydantic import BaseModel, Field
from typing import Optional

class UpdateCategoryRequest(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=255)
    