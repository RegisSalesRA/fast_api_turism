from pydantic import BaseModel, ConfigDict
from app.domain.entities.user_entity import UserRole
from datetime import datetime


class UserDetailResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    email: str
    role: UserRole
    created_at: datetime
    last_login: datetime | None
