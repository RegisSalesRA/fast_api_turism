from fastapi.params import Depends
from app.core.dependencies import get_db
from app.core.pagination.paginator import Paginator
from app.data.repository.category_repository_impl import CategoryRepositoryImpl
from app.data.repository.point_turism_repository_impl import PointTurismRepositoryImpl
from app.data.repository.city_repository_impl import CityRepositoryImpl
from app.data.repository.user_repository_impl import UserRepositoryImpl
from app.data.repository.review_repository_impl import ReviewRepositoryImpl
from app.data.repository.image_repository_impl import ImageRepositoryImpl
from app.data.repository.album_repository_impl import AlbumRepositoryImpl
from app.data.repository.favorite_repository_impl import FavoriteRepositoryImpl
from app.domain.usecases.category_usecase import CategoryUseCase
from app.domain.usecases.point_turism_usecase import PointTurismUseCase
from app.domain.usecases.city_usecase import CityUseCase
from app.domain.usecases.user_usecase import UserUseCase
from app.domain.usecases.review_usecase import ReviewUseCase
from app.domain.usecases.image_usecase import ImageUseCase
from app.domain.usecases.album_usecase import AlbumUseCase
from app.domain.usecases.favorite_usecase import FavoriteUseCase


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


async def get_user_usecase(db=Depends(get_db)):
    repo = UserRepositoryImpl(db)
    paginator = Paginator(db)
    usecase = UserUseCase(repo, paginator)
    return usecase


async def get_review_usecase(db=Depends(get_db)):
    repo = ReviewRepositoryImpl(db)
    paginator = Paginator(db)
    usecase = ReviewUseCase(repo, paginator)
    return usecase


async def get_image_usecase(db=Depends(get_db)):
    repo = ImageRepositoryImpl(db)
    paginator = Paginator(db)
    usecase = ImageUseCase(repo, paginator)
    return usecase


async def get_album_usecase(db=Depends(get_db)):
    repo = AlbumRepositoryImpl(db)
    paginator = Paginator(db)
    usecase = AlbumUseCase(repo, paginator)
    return usecase


async def get_favorite_usecase(db=Depends(get_db)):
    repo = FavoriteRepositoryImpl(db)
    usecase = FavoriteUseCase(repo)
    return usecase

