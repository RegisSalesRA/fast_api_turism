from fastapi.params import Depends 
from app.core.dependencies import get_db
from app.data.repository.category_repository_impl import CategoryRepositoryImpl
from app.data.repository.point_turism_repository_impl import PointTurismRepositoryImpl 
from app.domain.usecases.category_usecase import CategoryUseCase
from app.domain.usecases.point_turism_usecase import PointTurismUseCase 


def get_category_usecase(db=Depends(get_db)):
    repo = CategoryRepositoryImpl(db)
    usecase = CategoryUseCase(repo)
    return usecase


def get_points_turism_usecase(db=Depends(get_db)):
    repo = PointTurismRepositoryImpl(db)
    usecase = PointTurismUseCase(repo)
    return usecase

