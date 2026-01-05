from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class UpdateUserRequest(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255, description="Nome do usuário")
    email: Optional[EmailStr] = Field(None, description="Email do usuário")
