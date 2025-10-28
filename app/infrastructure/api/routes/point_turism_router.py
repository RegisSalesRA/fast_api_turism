from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.core.exceptions.domain_exceptions import NotFoundError
from app.data.repository.point_turism_repository_impl import PointTurismRepositoryImpl
from app.domain.entities.point_turism_entity import PointTurismEntity 
from app.domain.usecases.point_turism_service import PointTurismService
from app.infrastructure.api.schemas.point_turism.requests.create_point_turism import CreatePointTurismRequest
from app.infrastructure.api.schemas.point_turism.responses.point_turism_detail import PointTurismDetailResponse

router = APIRouter(prefix="/points", tags=["Points"])

def get_point_service(db: Session = Depends(get_db)) -> PointTurismService:
    repo = PointTurismRepositoryImpl(db)  
    return PointTurismService(repo)

@router.get("/", response_model=List[PointTurismDetailResponse])
def list_points(service: PointTurismService = Depends(get_point_service)):
    return service.list_points()

@router.get("/{point_id}", response_model=PointTurismDetailResponse)
def get_point(point_id: int, service: PointTurismService = Depends(get_point_service)):
    try:
        return service.get_point(point_id)
    except NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.post("/", response_model=PointTurismDetailResponse, status_code=status.HTTP_201_CREATED)
def create_point(payload: CreatePointTurismRequest, service: PointTurismService = Depends(get_point_service)):
    entity = PointTurismEntity(
        id=None,
        name=payload.name,
        image=payload.image,
        description=payload.description,
        city_id=1,
        category_id=2,
        review=0.0
    )
    created = service.create_point(entity)
    return created
