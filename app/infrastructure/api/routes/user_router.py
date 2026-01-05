from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List
from app.core.exceptions.domain_exceptions import NotFoundError
from app.core.injection_dependencies import get_user_usecase
from app.core.pagination.schemas import PageParams, PageResponse
from app.domain.entities.user_entity import UserEntity
from app.domain.usecases.user_usecase import UserUseCase
from app.utils.middleware import get_current_user
from app.data.models.user_model import UserModel
from app.infrastructure.api.schemas.user.request.create_user import CreateUserRequest
from app.infrastructure.api.schemas.user.request.update_user import UpdateUserRequest
from app.infrastructure.api.schemas.user.response.user_detail import UserDetailResponse


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=PageResponse[UserDetailResponse])
async def list_users(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    usecase: UserUseCase = Depends(get_user_usecase),
):
    page_params = PageParams(page=page, size=size)
    return await usecase.list_users(page_params)


@router.get("/{user_id}", response_model=UserDetailResponse)
async def get_user(user_id: str, usecase: UserUseCase = Depends(get_user_usecase)):
    try:
        return await usecase.get_user(user_id)
    except NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post("/", response_model=UserDetailResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    payload: CreateUserRequest,
    usecase: UserUseCase = Depends(get_user_usecase),
):
    entity = UserEntity(
        id=payload.id,
        name=payload.name,
        email=payload.email,
    )
    try:
        return await usecase.create_user(entity)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.put("/{user_id}", response_model=UserDetailResponse)
async def update_user(
    user_id: str,
    payload: UpdateUserRequest,
    usecase: UserUseCase = Depends(get_user_usecase),
    current_user: UserModel = Depends(get_current_user),
):
    """Atualizar usuário - Requer autenticação"""
    # Verificar se o usuário está atualizando a si mesmo
    if user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only update your own profile"
        )
    
    entity = UserEntity(
        id=user_id,
        name=payload.name,
        email=payload.email,
    )
    try:
        return await usecase.update_user(entity)
    except NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: str,
    usecase: UserUseCase = Depends(get_user_usecase),
    current_user: UserModel = Depends(get_current_user),
):
    """Deletar usuário - Requer autenticação"""
    # Verificar se o usuário está deletando a si mesmo
    if user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only delete your own profile"
        )
    
    try:
        await usecase.delete_user(user_id)
    except NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

