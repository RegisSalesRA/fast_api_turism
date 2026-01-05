from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.data.models.user_model import UserModel
from app.utils.middleware import get_current_user
from app.domain.entities.user_entity import UserRole

# HTTPBearer scheme
security = HTTPBearer()


async def get_current_admin_user(
    current_user: UserModel = Depends(get_current_user),
) -> UserModel:
    """
    Verifica se o usuário atual é admin
    
    Levanta HTTPException 403 se não for admin
    """
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only administrators can access this resource"
        )
    return current_user


async def get_current_user_or_admin(
    current_user: UserModel = Depends(get_current_user),
) -> UserModel:
    """
    Apenas valida que o usuário está autenticado
    Pode ser user ou admin
    """
    return current_user


async def verify_user_or_admin(
    user_id: str,
    current_user: UserModel = Depends(get_current_user),
) -> UserModel:
    """
    Verifica se o usuário é o próprio usuário ou admin
    Usado para atualizar/deletar perfil
    """
    if current_user.id != user_id and current_user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only modify your own profile or you need admin privileges"
        )
    return current_user
