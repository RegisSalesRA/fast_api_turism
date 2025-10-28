from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.core.exceptions.domain_exceptions import NotFoundError
from app.core.injection_dependencies import get_category_usecase
from app.domain.entities.category_entity import CategoryEntity
from app.domain.usecases.category_usecase import CategoryUseCase
from app.infrastructure.api.schemas.category.request.create_category import CreateCategoryRequest
from app.infrastructure.api.schemas.category.response.category_detail import CategoryDetailResponse

router = APIRouter(prefix="/categories", tags=["Categories"])



@router.get("/", response_model=List[CategoryDetailResponse])
def list_categories(useCase: CategoryUseCase = Depends(get_category_usecase)):
    return useCase.list_categorys()

@router.get("/{category_id}", response_model=CategoryDetailResponse)
def get_category(category_id: int, useCase: CategoryUseCase = Depends(get_category_usecase)):
    try:
        return useCase.get_category(category_id)
    except NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post("/", response_model=CategoryDetailResponse, status_code=status.HTTP_201_CREATED)
def create_category(payload: CreateCategoryRequest, useCase: CategoryUseCase = Depends(get_category_usecase)):
    entity = CategoryEntity(id=None, name=payload.name)
    return useCase.create_category(entity)


@router.put("/{category_id}", response_model=CategoryDetailResponse)
def update_category(category_id: int, payload: CreateCategoryRequest, useCase: CategoryUseCase = Depends(get_category_usecase)):
    entity = CategoryEntity(id=category_id, name=payload.name)
    try:
        return useCase.update_category(entity)
    except NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int, useCase: CategoryUseCase = Depends(get_category_usecase)):
    try:
        useCase.delete_category(category_id)
    except NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))



@router.get("/search/", response_model=List[CategoryDetailResponse])
def search_categories(name: str, useCase: CategoryUseCase = Depends(get_category_usecase)):
    return useCase.search_by_name(name)
