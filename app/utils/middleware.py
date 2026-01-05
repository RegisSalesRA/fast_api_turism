from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.auth.auth import verify_jwt_token
from app.core.dependencies import get_db
from app.data.models.user_model import UserModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

# HTTPBearer scheme - extrai token do header Authorization: Bearer <token>
security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
) -> UserModel:
    """Middleware para obter usuário atual do token JWT"""
    token = credentials.credentials
    user_id = verify_jwt_token(token)
    result = await db.execute(select(UserModel).filter(UserModel.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
