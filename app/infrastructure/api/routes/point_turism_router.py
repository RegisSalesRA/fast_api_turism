from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional 
from app.core.dependencies import get_db
from app.core.exceptions.domain_exceptions import NotFoundError
from app.core.injection_dependencies import get_points_turism_usecase 
from app.domain.entities.point_turism_entity import PointTurismEntity 
from app.domain.usecases.point_turism_usecase import PointTurismUseCase 
from app.infrastructure.api.schemas.point_turism.requests.create_point_turism import CreatePointTurismRequest
from app.infrastructure.api.schemas.point_turism.requests.update_point_turism import UpdatePointTurismRequest
from app.infrastructure.api.schemas.point_turism.responses.point_turism_detail import PointTurismDetailResponse

router = APIRouter(prefix="/points", tags=["Points"])

 
@router.get("/", response_model=List[PointTurismDetailResponse])
def list_points_turism(usecase: PointTurismUseCase = Depends(get_points_turism_usecase)):
    return usecase.list_points()

@router.get("/{point_id}", response_model=PointTurismDetailResponse)
def get_point_turism(point_id: int, usecase: PointTurismUseCase = Depends(get_points_turism_usecase)):
    try:
        return usecase.get_point(point_id)
    except NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.post("/", response_model=PointTurismDetailResponse, status_code=status.HTTP_201_CREATED)
def create_point_turism(payload: CreatePointTurismRequest, usecase: PointTurismUseCase = Depends(get_points_turism_usecase)):
    entity = PointTurismEntity(
        id=None,
        name=payload.name,
        image=payload.image,
        description=payload.description,
     
        category_id=2,
        review=0.0
    )
    created = usecase.create_point(entity)
    return created


@router.put("/{point_id}", response_model=PointTurismDetailResponse)
def update_point_turism(point_id: int, payload: UpdatePointTurismRequest, usecase: PointTurismUseCase = Depends(get_points_turism_usecase)):
    try:
        entity = PointTurismEntity(
            id=point_id,
            name=payload.name,
            image=payload.image,
            description=payload.description, 
            category_id=payload.category_id,
            review=payload.review
        )

        return usecase.update_point(entity)
    except NotFoundError as e:
        print('e ai?')
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    
@router.delete("/{point_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_point_turism(point_id: int, usecase: PointTurismUseCase = Depends(get_points_turism_usecase)):
    try:
        usecase.delete_point(point_id)
        return
    except NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    

@router.get("/search/", response_model=List[PointTurismDetailResponse])
def search_points_turism(name: str, usecase: PointTurismUseCase = Depends(get_points_turism_usecase)):
    return usecase.search_by_name(name)

@router.get("/filter/", response_model=List[PointTurismDetailResponse])
def filter_points_turism( 
    category_id: Optional[int] = None,
    min_review: Optional[float] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    usecase: PointTurismUseCase = Depends(get_points_turism_usecase)
):
    return usecase.filter_points( 
        category_id=category_id,
        min_review=min_review,
        limit=limit,
        offset=offset
    )