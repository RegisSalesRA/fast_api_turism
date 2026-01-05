from pydantic import BaseModel, EmailStr
from datetime import datetime
from app.domain.entities.user_entity import UserRole


class UserResponse(BaseModel):
    """Schema para retornar dados do usuário (sem senha)"""
    id: str
    name: str
    email: EmailStr
    role: UserRole
    created_at: datetime
    last_login: datetime | None = None

    model_config = {"from_attributes": True}


class UserDetailResponse(UserResponse):
    """Detalhes completos do usuário autenticado"""
    updated_at: datetime

    model_config = {"from_attributes": True}
