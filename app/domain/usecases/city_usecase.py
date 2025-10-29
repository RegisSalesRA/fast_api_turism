from typing import List, Optional
from app.core.exceptions.domain_exceptions import NotFoundError
from app.domain.entities.city_entity import CityEntity
from app.domain.repositories.city_repository import CityRepository


class CityUseCase:

    def __init__(self, repository: CityRepository):
        self.repo = repository

    def create_city(self, entity: CityEntity) -> CityEntity:
        if not entity.name or entity.name.strip() == "":
            raise ValueError("name must not be empty")
        if not entity.state or entity.state.strip() == "":
            raise ValueError("state must not be empty")
        created = self.repo.create(entity)
        return created

    def list_cities(self, *, limit: Optional[int] = None, offset: Optional[int] = None) -> List[CityEntity]:
        return self.repo.list_all(limit=limit, offset=offset)

    def get_city(self, id: int) -> CityEntity:
        c = self.repo.get_by_id(id)
        if c is None:
            raise NotFoundError(f"City with id {id} not found")
        return c

    def update_city(self, entity: CityEntity) -> CityEntity:
        if not entity.name or entity.name.strip() == "":
            raise ValueError("name must not be empty")
        if not entity.state or entity.state.strip() == "":
            raise ValueError("state must not be empty")
        updated = self.repo.update(entity)
        if updated is None:
            raise NotFoundError(f"City with id {entity.id} not found")
        return updated

    def delete_city(self, id: int) -> None:
        deleted = self.repo.delete(id)
        if not deleted:
            raise NotFoundError(f"City with id {id} not found")

    def search_by_name(self, name: str) -> List[CityEntity]:
        return self.repo.search_by_name(name)

