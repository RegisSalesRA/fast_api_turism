from pydantic import BaseModel, Field, EmailStr


class CreateUserRequest(BaseModel):
    id: str = Field(..., min_length=1, description="ID do usuário")
    name: str = Field(..., min_length=1, max_length=255, description="Nome do usuário")
    email: EmailStr = Field(..., description="Email do usuário")
