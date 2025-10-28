from pydantic import BaseModel
from typing import Optional

class FilterPointTurismRequest(BaseModel):
    name: Optional[str] = None 