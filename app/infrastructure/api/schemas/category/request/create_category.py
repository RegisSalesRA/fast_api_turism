from pydantic import BaseModel, Field 

class CreateCategoryRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=255)
