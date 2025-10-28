from typing import List, Optional
from app.core.exceptions.domain_exceptions import NotFoundError
from app.domain.entities.point_turism_entity import PointTurismEntity
from app.domain.repositories.point_turism_repository import PointTurismRepository
 
class PointTurismService: 

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
        existing = self.repo.get_by_id(entity.id)
        if existing is None:
            raise NotFoundError(f"Point with id {entity.id} not found")

        existing.name = entity.name or existing.name
        existing.image = entity.image or existing.image
        existing.description = entity.description if entity.description is not None else existing.description
        existing.city_id = entity.city_id or existing.city_id
        existing.category_id = entity.category_id or existing.category_id
        existing.review = entity.review if entity.review is not None else existing.review

        updated = self.repo.update(existing)
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
        city_id: Optional[int] = None,
        category_id: Optional[int] = None,
        min_review: Optional[float] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> List[PointTurismEntity]:
        return self.repo.filter(city_id=city_id, category_id=category_id, min_review=min_review, limit=limit, offset=offset)

    def summary_by_city(self):
        """
        Ex: retorna lista de dicts: [{ 'city_id': 1, 'city_name': 'X', 'total_points': 5, 'average_review': 4.2 }, ...]
        Implementação delegada ao repositório (consulta agregada).
        """
        return self.repo.summary_by_city()
