from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List
from app.core.exceptions.domain_exceptions import NotFoundError
from app.core.injection_dependencies import get_favorite_usecase
from app.data.models.user_model import UserModel
from app.domain.entities.favorite_entity import FavoriteEntity
from app.domain.usecases.favorite_usecase import FavoriteUseCase
from app.infrastructure.api.schemas.favorite.request.create_favorite import CreateFavoriteRequest
from app.infrastructure.api.schemas.favorite.response.favorite_detail import FavoriteDetailResponse
from app.utils.middleware import get_current_user

router = APIRouter(prefix="/favorites", tags=["Favorites"])


@router.get("/", response_model=List[FavoriteDetailResponse])
async def list_favorites(
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    usecase: FavoriteUseCase = Depends(get_favorite_usecase),
):
    return await usecase.list_favorites(limit, offset)


@router.get("/user/{user_id}", response_model=List[FavoriteDetailResponse])
async def get_user_favorites(
    user_id: str,
    usecase: FavoriteUseCase = Depends(get_favorite_usecase),
):
    return await usecase.get_user_favorites(user_id)


@router.get("/{user_id}/{point_turism_id}", response_model=dict)
async def is_favorite(
    user_id: str,
    point_turism_id: int,
    usecase: FavoriteUseCase = Depends(get_favorite_usecase),
):
    is_fav = await usecase.is_favorite(user_id, point_turism_id)
    return {"is_favorite": is_fav}


@router.post("/", response_model=FavoriteDetailResponse, status_code=status.HTTP_201_CREATED)
async def create_favorite(
    payload: CreateFavoriteRequest,
    usecase: FavoriteUseCase = Depends(get_favorite_usecase),
    current_user: UserModel = Depends(get_current_user),
):
    """Criar favorito - 👤 SOMENTE USUÁRIO AUTENTICADO"""
    entity = FavoriteEntity(
        user_id=payload.user_id,
        point_turism_id=payload.point_turism_id,
    )
    try:
        return await usecase.add_favorite(entity)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{user_id}/{point_turism_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_favorite(
    user_id: str,
    point_turism_id: int,
    usecase: FavoriteUseCase = Depends(get_favorite_usecase),
    current_user: UserModel = Depends(get_current_user),
):
    """Remover favorito - 👤 SOMENTE USUÁRIO AUTENTICADO"""
    try:
        await usecase.remove_favorite(user_id, point_turism_id)
    except NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
