from pydantic import BaseModel, ConfigDict

class CityDetailResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    state: str
    country: str
    description: str | None

