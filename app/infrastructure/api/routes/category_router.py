from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List
from app.core.exceptions.domain_exceptions import NotFoundError
from app.core.injection_dependencies import get_category_usecase
from app.core.pagination.schemas import PageParams, PageResponse
from app.domain.entities.category_entity import CategoryEntity
from app.domain.usecases.category_usecase import CategoryUseCase
from app.utils.middleware import get_current_user
from app.utils.permissions import get_current_admin_user
from app.data.models.user_model import UserModel
from app.infrastructure.api.schemas.category.request.create_category import CreateCategoryRequest
from app.infrastructure.api.schemas.category.response.category_detail import CategoryDetailResponse

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/", response_model=PageResponse[CategoryDetailResponse])
async def list_categories(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    useCase: CategoryUseCase = Depends(get_category_usecase)
):
    """Listar categorias - Público"""
    page_params = PageParams(page=page, size=size)
    return await useCase.list_categories(page_params)


@router.get("/{category_id}", response_model=CategoryDetailResponse)
async def get_category(category_id: int, useCase: CategoryUseCase = Depends(get_category_usecase)):
    """Obter categoria específica - Público"""
    try:
        return await useCase.get_category(category_id)
    except NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post("/", response_model=CategoryDetailResponse, status_code=status.HTTP_201_CREATED)
async def create_category(
    payload: CreateCategoryRequest,
    useCase: CategoryUseCase = Depends(get_category_usecase),
    current_admin: UserModel = Depends(get_current_admin_user)
):
    """Criar categoria - ⛔ SOMENTE ADMIN"""
    entity = CategoryEntity(id=None, name=payload.name)
    return await useCase.create_category(entity)


@router.put("/{category_id}", response_model=CategoryDetailResponse)
async def update_category(
    category_id: int,
    payload: CreateCategoryRequest,
    useCase: CategoryUseCase = Depends(get_category_usecase),
    current_admin: UserModel = Depends(get_current_admin_user)
):
    """Atualizar categoria - ⛔ SOMENTE ADMIN"""
    entity = CategoryEntity(id=category_id, name=payload.name)
    try:
        return await useCase.update_category(entity)
    except NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(
    category_id: int,
    useCase: CategoryUseCase = Depends(get_category_usecase),
    current_admin: UserModel = Depends(get_current_admin_user)
):
    """Deletar categoria - ⛔ SOMENTE ADMIN"""
    try:
        await useCase.delete_category(category_id)
    except NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/search/", response_model=List[CategoryDetailResponse])
async def search_categories(name: str, useCase: CategoryUseCase = Depends(get_category_usecase)):
    """Buscar categorias por nome - Público"""
    return await useCase.search_by_name(name)
