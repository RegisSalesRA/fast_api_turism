from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.dependencies import get_db
from app.domain.usecases.auth_usecase import AuthUseCase
from app.data.repository.user_repository_impl import UserRepositoryImpl
from app.utils.middleware import get_current_user
from app.data.models.user_model import UserModel
from app.infrastructure.api.schemas.auth_schema import (
    LoginRequest,
    LoginResponse,
    RegisterRequest,
    RegisterResponse,
)
from app.infrastructure.api.schemas.user_schema import UserDetailResponse

router = APIRouter(prefix="/auth", tags=["authentication"])


async def get_auth_use_case(db: AsyncSession = Depends(get_db)) -> AuthUseCase:
    """Injetar AuthUseCase com UserRepository"""
    user_repo = UserRepositoryImpl(db)
    return AuthUseCase(user_repo)


@router.post("/register", response_model=RegisterResponse, status_code=status.HTTP_201_CREATED)
async def register(
    request: RegisterRequest,
    auth_usecase: AuthUseCase = Depends(get_auth_use_case)
) -> RegisterResponse:
    """
    Registrar novo usuário
    
    - **name**: Nome completo do usuário
    - **email**: Email único
    - **password**: Senha (será hasheada)
    """
    result = await auth_usecase.register(
        email=request.email,
        password=request.password,
        name=request.name
    )
    
    return RegisterResponse(
        access_token=result["access_token"],
        token_type=result["token_type"],
        user_id=result["user_id"],
        email=result["email"],
        name=result["name"],
    )


@router.post("/login", response_model=LoginResponse)
async def login(
    request: LoginRequest,
    auth_usecase: AuthUseCase = Depends(get_auth_use_case)
) -> LoginResponse:
    """
    Fazer login e obter JWT token
    
    - **email**: Email do usuário
    - **password**: Senha do usuário
    """
    result = await auth_usecase.login(
        email=request.email,
        password=request.password
    )
    
    return LoginResponse(
        access_token=result["access_token"],
        token_type=result["token_type"],
        user_id=result["user_id"],
    )


@router.get("/me", response_model=UserDetailResponse)
async def get_current_user_info(
    current_user: UserModel = Depends(get_current_user)
) -> UserModel:
    """
    Obter informações do usuário autenticado
    
    Requer JWT token no header:
    ```
    Authorization: Bearer <seu_token>
    ```
    """
    return current_user

