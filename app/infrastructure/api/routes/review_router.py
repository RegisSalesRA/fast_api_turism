from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List
from app.core.exceptions.domain_exceptions import NotFoundError
from app.core.injection_dependencies import get_review_usecase
from app.core.pagination.schemas import PageParams, PageResponse
from app.data.models.user_model import UserModel, UserRole
from app.domain.entities.review_entity import ReviewEntity
from app.domain.usecases.review_usecase import ReviewUseCase
from app.infrastructure.api.schemas.review.request.create_review import CreateReviewRequest
from app.infrastructure.api.schemas.review.request.update_review import UpdateReviewRequest
from app.infrastructure.api.schemas.review.response.review_detail import ReviewDetailResponse
from app.utils.middleware import get_current_user

router = APIRouter(prefix="/reviews", tags=["Reviews"])


@router.get("/", response_model=PageResponse[ReviewDetailResponse])
async def list_reviews(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    usecase: ReviewUseCase = Depends(get_review_usecase),
):
    page_params = PageParams(page=page, size=size)
    return await usecase.list_reviews(page_params)


@router.get("/point-turism/{point_turism_id}", response_model=List[ReviewDetailResponse])
async def get_reviews_by_point_turism(
    point_turism_id: int,
    usecase: ReviewUseCase = Depends(get_review_usecase),
):
    return await usecase.get_reviews_by_point_turism(point_turism_id)


@router.get("/me", response_model=List[ReviewDetailResponse])
async def get_my_reviews(
    usecase: ReviewUseCase = Depends(get_review_usecase),
    current_user: UserModel = Depends(get_current_user),
):
    """Listar minhas avaliações - 👤 SOMENTE USUÁRIO AUTENTICADO"""
    return await usecase.get_reviews_by_user(current_user.id)


@router.post("/", response_model=ReviewDetailResponse, status_code=status.HTTP_201_CREATED)
async def create_review(
    payload: CreateReviewRequest,
    usecase: ReviewUseCase = Depends(get_review_usecase),
    current_user: UserModel = Depends(get_current_user),
):
    """Criar avaliação - 👤 SOMENTE USUÁRIO AUTENTICADO"""
    entity = ReviewEntity(
        id=None,
        user_id=current_user.id,
        point_turism_id=payload.point_turism_id,
        rating=payload.rating,
        comment=payload.comment,
    )
    try:
        return await usecase.create_review(entity)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.put("/{point_turism_id}", response_model=ReviewDetailResponse)
async def update_my_review(
    point_turism_id: int,
    payload: UpdateReviewRequest,
    usecase: ReviewUseCase = Depends(get_review_usecase),
    current_user: UserModel = Depends(get_current_user),
):
    """Atualizar minha avaliação para um ponto - 👤 SOMENTE USUÁRIO AUTENTICADO"""
    try:
        return await usecase.update_my_review(
            user_id=current_user.id,
            point_turism_id=point_turism_id,
            rating=payload.rating,
            comment=payload.comment,
        )
    except NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{point_turism_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_my_review(
    point_turism_id: int,
    usecase: ReviewUseCase = Depends(get_review_usecase),
    current_user: UserModel = Depends(get_current_user),
):
    """Deletar minha avaliação para um ponto - 👤 SOMENTE USUÁRIO AUTENTICADO"""
    try:
        await usecase.delete_my_review(current_user.id, point_turism_id)
    except NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


