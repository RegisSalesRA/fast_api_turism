from pydantic import BaseModel, ConfigDict
from app.domain.entities.user_entity import UserRole


class UserSummaryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    email: str
    role: UserRole
