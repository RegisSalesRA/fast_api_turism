from fastapi import APIRouter, Depends, HTTPException, status, Query
from app.core.exceptions.domain_exceptions import NotFoundError
from app.core.injection_dependencies import get_album_usecase, get_image_usecase
from app.core.pagination.schemas import PageParams, PageResponse
from app.domain.entities.album_entity import AlbumEntity
from app.domain.entities.image_entity import ImageEntity
from app.domain.usecases.album_usecase import AlbumUseCase
from app.domain.usecases.image_usecase import ImageUseCase
from app.utils.permissions import get_current_admin_user
from app.data.models.user_model import UserModel
from app.infrastructure.api.schemas.album.request.create_album import CreateAlbumRequest
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
async def get_album(album_id: int, usecase: AlbumUseCase = Depends(get_album_usecase)):
    try:
        return await usecase.get_album(album_id)
    except NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post("/", response_model=AlbumDetailResponse, status_code=status.HTTP_201_CREATED)
async def create_album(
    payload: CreateAlbumRequest,
    usecase: AlbumUseCase = Depends(get_album_usecase),
    image_usecase: ImageUseCase = Depends(get_image_usecase),
    current_admin: UserModel = Depends(get_current_admin_user)
):
    """Criar album com imagens - ⛔ SOMENTE ADMIN"""
    # Criar imagens primeiro se fornecidas
    images = []
    if payload.image_urls:
        for url in payload.image_urls:
            image_entity = ImageEntity(
                id=None,
                url=str(url),
                album_id=None,  # Will be set after album is created
            )
            try:
                created_image = await image_usecase.create_image(image_entity)
                images.append(created_image)
            except ValueError as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
    # Criar album
    entity = AlbumEntity(
        id=None,
        title=payload.title,
        description=payload.description,
        images=images,
    )
    return await usecase.create_album(entity)


@router.put("/{album_id}", response_model=AlbumDetailResponse)
async def update_album(
    album_id: int,
    payload: UpdateAlbumRequest,
    usecase: AlbumUseCase = Depends(get_album_usecase),
    current_admin: UserModel = Depends(get_current_admin_user)
):
    """Atualizar album - ⛔ SOMENTE ADMIN"""
    entity = AlbumEntity(
        id=album_id,
        title=payload.title,
        description=payload.description,
    )
    try:
        return await usecase.update_album(entity)
    except NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{album_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_album(
    album_id: int,
    usecase: AlbumUseCase = Depends(get_album_usecase),
    current_admin: UserModel = Depends(get_current_admin_user)
):
    """Deletar album - ⛔ SOMENTE ADMIN"""
    try:
        await usecase.delete_album(album_id)
    except NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post("/{album_id}/images/{image_id}", status_code=status.HTTP_204_NO_CONTENT)
async def add_image_to_album(
    album_id: int,
    image_id: int,
    usecase: AlbumUseCase = Depends(get_album_usecase),
    current_admin: UserModel = Depends(get_current_admin_user)
):
    """Adicionar imagem ao album - ⛔ SOMENTE ADMIN"""
    try:
        await usecase.add_image_to_album(album_id, image_id)
    except NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{album_id}/images/{image_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_image_from_album(
    album_id: int,
    image_id: int,
    usecase: AlbumUseCase = Depends(get_album_usecase),
):
    try:
        await usecase.remove_image_from_album(album_id, image_id)
    except NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
