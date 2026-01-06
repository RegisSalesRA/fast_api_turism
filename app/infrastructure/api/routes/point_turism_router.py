from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional

from app.core.exceptions.domain_exceptions import NotFoundError
from app.core.injection_dependencies import get_points_turism_usecase
from app.domain.usecases.point_turism_usecase import PointTurismUseCase
from app.utils.permissions import get_current_admin_user
from app.data.models.user_model import UserModel
from app.infrastructure.api.schemas.point_turism.requests.create_point_turism import CreatePointTurismRequest
from app.infrastructure.api.schemas.point_turism.requests.update_point_turism import UpdatePointTurismRequest
from app.infrastructure.api.schemas.point_turism.responses.point_turism_detail import PointTurismDetailResponse

router = APIRouter(prefix="/points", tags=["Points"])


@router.get("/", response_model=List[PointTurismDetailResponse])
async def list_points(
    usecase: PointTurismUseCase = Depends(get_points_turism_usecase)
):
    return await usecase.list_points()


@router.get("/{point_id}", response_model=PointTurismDetailResponse)
async def get_point(
    point_id: int,
    usecase: PointTurismUseCase = Depends(get_points_turism_usecase)
):
    try:
        return await usecase.get_point(point_id)
    except NotFoundError as e:
        raise HTTPException(404, str(e))


@router.post("/", response_model=PointTurismDetailResponse, status_code=201)
async def create_point(
    payload: CreatePointTurismRequest,
    usecase: PointTurismUseCase = Depends(get_points_turism_usecase),
    current_admin: UserModel = Depends(get_current_admin_user)
):
    """Criar ponto turístico - ⛔ SOMENTE ADMIN"""
    return await usecase.create_point(payload.to_entity())


@router.put("/{point_id}", response_model=PointTurismDetailResponse)
async def update_point(
    point_id: int,
    payload: UpdatePointTurismRequest,
    usecase: PointTurismUseCase = Depends(get_points_turism_usecase),
    current_admin: UserModel = Depends(get_current_admin_user)
):
    """Atualizar ponto turístico - ⛔ SOMENTE ADMIN"""
    try:
        return await usecase.update_point(payload.to_entity(point_id))
    except NotFoundError as e:
        raise HTTPException(404, str(e))


@router.delete("/{point_id}", status_code=204)
async def delete_point(
    point_id: int,
    usecase: PointTurismUseCase = Depends(get_points_turism_usecase),
    current_admin: UserModel = Depends(get_current_admin_user)
):
    """Deletar ponto turístico - ⛔ SOMENTE ADMIN"""
    try:
        await usecase.delete_point(point_id)
    except NotFoundError as e:
        raise HTTPException(404, str(e))
