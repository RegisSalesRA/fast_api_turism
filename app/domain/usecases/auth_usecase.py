from app.auth.auth import get_password_hash, verify_password, create_access_token
from app.domain.entities.user_entity import UserEntity, UserRole
from app.domain.repositories.user_repository import UserRepository
from fastapi import HTTPException, status
import uuid


class AuthUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repo = user_repository

    async def register(
        self,
        email: str,
        password: str,
        name: str,
        role: UserRole = UserRole.USER
    ) -> dict:
        """Registrar novo usuário"""
        # Verificar se usuário já existe
        existing_user = await self.user_repo.get_by_email(email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

        # Gerar ID único para o usuário
        user_id = str(uuid.uuid4())
        
        # Hash da senha
        hashed_password = get_password_hash(password)
        
        # Criar entidade de usuário com role especificado
        user_entity = UserEntity(
            id=user_id,
            name=name,
            email=email,
            role=role,
        )
        
        # Salvar usuário com senha hasheada
        created_user = await self.user_repo.create(user_entity, password_hash=hashed_password)
        
        # Gerar token JWT
        access_token = create_access_token(data={"sub": user_id})
        
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user_id": created_user.id,
            "email": created_user.email,
            "name": created_user.name,
        }

    async def login(self, email: str, password: str) -> dict:
        """Fazer login e gerar JWT token"""
        # Buscar usuário por email com password hash
        user_data = await self.user_repo.get_user_by_email_with_password(email)
        if not user_data:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )

        user, password_hash = user_data
        
        # Verificar senha
        if not verify_password(password, password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )
        
        # Gerar token JWT
        access_token = create_access_token(data={"sub": user.id})
        
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user_id": user.id
        }
