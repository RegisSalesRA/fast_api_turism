from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List
from app.core.exceptions.domain_exceptions import NotFoundError
from app.core.injection_dependencies import get_city_usecase
from app.core.pagination.schemas import PageParams, PageResponse
from app.domain.entities.city_entity import CityEntity
from app.domain.usecases.city_usecase import CityUseCase
from app.infrastructure.api.schemas.city.request.create_city import CreateCityRequest
from app.infrastructure.api.schemas.city.request.update_city import UpdateCityRequest
from app.infrastructure.api.schemas.city.response.get_city_detail import CityDetailResponse

router = APIRouter(prefix="/cities", tags=["Cities"])


@router.get("/", response_model=PageResponse[CityDetailResponse])
async def list_cities(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    usecase: CityUseCase = Depends(get_city_usecase),
):
    page_params = PageParams(page=page, size=size)
    return await usecase.list_cities(page_params)


@router.get("/search/", response_model=List[CityDetailResponse])
async def search_cities_by_name(
    name: str,
    usecase: CityUseCase = Depends(get_city_usecase),
):
    return await usecase.search_by_name(name)


@router.get("/{city_id}", response_model=CityDetailResponse)
async def get_city(city_id: int, usecase: CityUseCase = Depends(get_city_usecase)):
    try:
        return await usecase.get_city(city_id)
    except NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post("/", response_model=CityDetailResponse, status_code=status.HTTP_201_CREATED)
async def create_city(
    payload: CreateCityRequest,
    usecase: CityUseCase = Depends(get_city_usecase),
):
    entity = CityEntity(
        id=None,
        name=payload.name,
        state=payload.state,
        country=payload.country,
        description=payload.description,
    )
    return await usecase.create_city(entity)


@router.put("/{city_id}", response_model=CityDetailResponse)
async def update_city(
    city_id: int,
    payload: UpdateCityRequest,
    usecase: CityUseCase = Depends(get_city_usecase),
):
    entity = CityEntity(
        id=city_id,
        name=payload.name,
        state=payload.state,
        country=payload.country,
        description=payload.description,
    )
    try:
        return await usecase.update_city(entity)
    except NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{city_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_city(city_id: int, usecase: CityUseCase = Depends(get_city_usecase)):
    try:
        await usecase.delete_city(city_id)
    except NotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
