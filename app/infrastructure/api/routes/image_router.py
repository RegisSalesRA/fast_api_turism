from fastapi import APIRouter, Depends, HTTPException, status, Query
from app.core.exceptions.domain_exceptions import NotFoundError
from app.core.injection_dependencies import get_image_usecase
from app.core.pagination.schemas import PageParams, PageResponse
from app.domain.entities.image_entity import ImageEntity
from app.domain.usecases.image_usecase import ImageUseCase
from app.utils.permissions import get_current_admin_user
from app.data.models.user_model import UserModel
from app.infrastructure.api.schemas.image.request.create_image import CreateImageRequest
from app.infrastructure.api.schemas.image.request.update_image import UpdateImageRequest
from app.infrastructure.api.schemas.image.response.image_detail import ImageDetailResponse

router = APIRouter(prefix="/images", tags=["Images"])


@router.get("/", response_model=PageResponse[ImageDetailResponse])
async def list_images(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    usecase: ImageUseCase = Depends(get_image_usecase),
):
    page_params = PageParams(page=page, size=size)
    return await usecase.list_images(page_params)


@router.get("/{image_id}", response_model=ImageDetailResponse)
async def get_image(image_id: int, usecase: ImageUseCase = Depends(get_image_usecase)):
    try:
        return await usecase.get_image(image_id)
    except NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post("/", response_model=ImageDetailResponse, status_code=status.HTTP_201_CREATED)
async def create_image(
    payload: CreateImageRequest,
    usecase: ImageUseCase = Depends(get_image_usecase),
    current_admin: UserModel = Depends(get_current_admin_user)
):
    """Criar imagem - ⛔ SOMENTE ADMIN"""
    entity = ImageEntity(
        id=None,
        url=str(payload.url),
        album_id=payload.album_id,
        point_turism_id=payload.point_turism_id,
    )
    try:
        return await usecase.create_image(entity)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.put("/{image_id}", response_model=ImageDetailResponse)
async def update_image(
    image_id: int,
    payload: UpdateImageRequest,
    usecase: ImageUseCase = Depends(get_image_usecase),
    current_admin: UserModel = Depends(get_current_admin_user)
):
    """Atualizar imagem - ⛔ SOMENTE ADMIN"""
    entity = ImageEntity(
        id=image_id,
        url=str(payload.url) if payload.url else None,
    )
    try:
        return await usecase.update_image(entity)
    except NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/{image_id}/point-turism/{point_turism_id}", status_code=status.HTTP_204_NO_CONTENT)
async def associate_image_to_point_turism(
    image_id: int,
    point_turism_id: int,
    usecase: ImageUseCase = Depends(get_image_usecase),
    current_admin: UserModel = Depends(get_current_admin_user)
):
    """Associar imagem a um ponto turístico - ⛔ SOMENTE ADMIN"""
    try:
        await usecase.associate_image_to_point_turism(image_id, point_turism_id)
    except NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{image_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_image(
    image_id: int,
    usecase: ImageUseCase = Depends(get_image_usecase),
    current_admin: UserModel = Depends(get_current_admin_user)
):
    """Deletar imagem - ⛔ SOMENTE ADMIN"""
    try:
        await usecase.delete_image(image_id)
    except NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
