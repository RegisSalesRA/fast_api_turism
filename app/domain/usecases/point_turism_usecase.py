from typing import List, Optional
from app.core.exceptions.domain_exceptions import NotFoundError
from app.domain.entities.point_turism_entity import PointTurismEntity
from app.domain.repositories.point_turism_repository import PointTurismRepository
 
class PointTurismUseCase: 

    def __init__(self, repository: PointTurismRepository):
        self.repo = repository

    def create_point(self, entity: PointTurismEntity) -> PointTurismEntity:
        if not entity.name or entity.name.strip() == "":
            raise ValueError("name must not be empty")
        created = self.repo.create(entity)
        return created

    def list_points(self, *, limit: Optional[int] = None, offset: Optional[int] = None) -> List[PointTurismEntity]:
        return self.repo.list_all(limit=limit, offset=offset)

    def get_point(self, id: int) -> PointTurismEntity:
        p = self.repo.get_by_id(id)
        if p is None:
            raise NotFoundError(f"Point with id {id} not found")
        return p

    def update_point(self, entity: PointTurismEntity) -> PointTurismEntity:
        print("fudeu?")
        existing = self.repo.get_by_id(entity.id)
        if existing is None:
            raise NotFoundError(f"Point with id {entity.id} not found")

        updated = self.repo.update(entity)
        return updated
 
    def delete_point(self, id: int) -> None:
        existing = self.repo.get_by_id(id)
        if existing is None:
            raise NotFoundError(f"Point with id {id} not found")
        self.repo.delete(id)

    def search_by_name(self, name: str) -> List[PointTurismEntity]:
        if not name:
            return []
        return self.repo.search_by_name(name)

    def filter_points(
        self,
       
        category_id: Optional[int] = None,
        min_review: Optional[float] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> List[PointTurismEntity]:
        return self.repo.filter(  category_id=category_id, min_review=min_review, limit=limit, offset=offset)
 