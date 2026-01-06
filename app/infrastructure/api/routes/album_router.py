from fastapi import APIRouter, Depends, HTTPException, status, Query
from app.core.exceptions.domain_exceptions import NotFoundError
from app.core.injection_dependencies import get_album_usecase
from app.core.pagination.schemas import PageParams, PageResponse
from app.domain.entities.album_entity import AlbumEntity
from app.domain.usecases.album_usecase import AlbumUseCase
from app.utils.permissions import get_current_admin_user
from app.data.models.user_model import UserModel
from app.infrastructure.api.schemas.album.request.create_album import AlbumCreateSchema
from app.infrastructure.api.schemas.album.request.update_album import UpdateAlbumRequest
from app.infrastructure.api.schemas.album.response.album_detail import AlbumDetailResponse

router = APIRouter(prefix="/albums", tags=["Albums"])


@router.get("/", response_model=PageResponse[AlbumDetailResponse])
async def list_albums(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    usecase: AlbumUseCase = Depends(get_album_usecase),
):
    page_params = PageParams(page=page, size=size)
    return await usecase.list_albums(page_params)


@router.get("/{album_id}", response_model=AlbumDetailResponse)
async def get_album(
    album_id: int,
    usecase: AlbumUseCase = Depends(get_album_usecase),
):
    try:
        return await usecase.get_album(album_id)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post(
    "/",
    response_model=AlbumDetailResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_album(
    payload: AlbumCreateSchema,
    usecase: AlbumUseCase = Depends(get_album_usecase),
    current_admin: UserModel = Depends(get_current_admin_user),
):
    entity = AlbumEntity(
        id=None,
        point_turism_id=payload.point_turism_id,
        image_urls=[str(url) for url in payload.image_urls],
    )
    return await usecase.create_album(entity)


@router.put("/{album_id}", response_model=AlbumDetailResponse)
async def update_album(
    album_id: int,
    payload: UpdateAlbumRequest,
    usecase: AlbumUseCase = Depends(get_album_usecase),
    current_admin: UserModel = Depends(get_current_admin_user),
):
    entity = AlbumEntity(
        id=album_id,
        image_urls=[str(url) for url in payload.image_urls]
        if payload.image_urls is not None
        else None,
    )
    try:
        return await usecase.update_album(entity)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{album_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_album(
    album_id: int,
    usecase: AlbumUseCase = Depends(get_album_usecase),
    current_admin: UserModel = Depends(get_current_admin_user),
):
    try:
        await usecase.delete_album(album_id)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
