from pydantic import BaseModel, Field
from typing import Optional 
from pydantic import BaseModel, HttpUrl, conlist

class AlbumCreateSchema(BaseModel):
    point_turism_id: int
    image_urls: conlist(HttpUrl, max_length=10) # type: ignore