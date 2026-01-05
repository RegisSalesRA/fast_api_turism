from pydantic import BaseModel, ConfigDict


class ImageDetailResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    url: str
