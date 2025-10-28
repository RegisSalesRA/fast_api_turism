from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.core.exceptions.domain_exceptions import NotFoundError
from app.data.repository.category_repository_impl import CategoryRepositoryImpl
from app.domain.entities.category_entity import CategoryEntity
from app.domain.services.category_service import CategoryService
from app.infrastructure.api.schemas.category.request.create_category import CreateCategoryRequest
from app.infrastructure.api.schemas.category.response.category_detail import CategoryDetailResponse 

router = APIRouter(prefix="/category", tags=["Category"])

def get_point_service(db: Session = Depends(get_db)) -> CategoryService:
    repo = CategoryRepositoryImpl(db)  
    return CategoryService(repo)

@router.get("/", response_model=List[CategoryDetailResponse])
def list_points(service: CategoryService = Depends(get_point_service)):
    return service.list_points()

@router.get("/{point_id}", response_model=CategoryDetailResponse)
def get_point(point_id: int, service: CategoryService = Depends(get_point_service)):
    try:
        return service.get_point(point_id)
    except NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.post("/", response_model=CategoryDetailResponse, status_code=status.HTTP_201_CREATED)
def create_point(payload: CreateCategoryRequest, service: CategoryService = Depends(get_point_service)):
    entity = CategoryEntity(
        id=None,
        name=payload.name 
    )
    created = service.create_point(entity)
    return created
