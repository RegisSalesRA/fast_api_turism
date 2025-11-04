from fastapi.params import Depends
from app.core.dependencies import get_db
from app.core.pagination.paginator import Paginator
from app.data.repository.category_repository_impl import CategoryRepositoryImpl
from app.data.repository.point_turism_repository_impl import PointTurismRepositoryImpl
from app.data.repository.city_repository_impl import CityRepositoryImpl
from app.domain.usecases.category_usecase import CategoryUseCase
from app.domain.usecases.point_turism_usecase import PointTurismUseCase
from app.domain.usecases.city_usecase import CityUseCase


async def get_category_usecase(db=Depends(get_db)):
    repo = CategoryRepositoryImpl(db)
    paginator = Paginator(db)
    usecase = CategoryUseCase(repo, paginator)
    return usecase


def get_points_turism_usecase(db=Depends(get_db)):
    repo = PointTurismRepositoryImpl(db)
    city_repo = CityRepositoryImpl(db)
    category_repo = CategoryRepositoryImpl(db)
    usecase = PointTurismUseCase(repo, city_repo, category_repo)
    return usecase


async def get_city_usecase(db=Depends(get_db)):
    repo = CityRepositoryImpl(db)
    pagintator = Paginator(db)
    usecase = CityUseCase(repo, paginator=pagintator)
    return usecase

