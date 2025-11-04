from typing import List, Optional
from app.core.exceptions.domain_exceptions import NotFoundError
from app.core.pagination.paginator import Paginator
from app.core.pagination.schemas import PageParams
from app.domain.entities.city_entity import CityEntity
from app.domain.repositories.city_repository import CityRepository


class CityUseCase:

    def __init__(self, repository: CityRepository, paginator: Paginator):
        self.repo = repository
        self.paginator = paginator

    async def create_city(self, entity: CityEntity) -> CityEntity:
        if not entity.name or entity.name.strip() == "":
            raise ValueError("name must not be empty")
        if not entity.state or entity.state.strip() == "":
            raise ValueError("state must not be empty")
        created = await self.repo.create(entity)
        return created

    async def list_cities(self,page_params: PageParams) -> List[CityEntity]:
        query = self.repo.base_query()  
        return await self.paginator.paginate(query, page_params, CityEntity)

    async def get_city(self, id: int) -> CityEntity:
        c = await self.repo.get_by_id(id)
        if c is None:
            raise NotFoundError(f"City with id {id} not found")
        return c

    async def update_city(self, entity: CityEntity) -> CityEntity:
        if not entity.name or entity.name.strip() == "":
            raise ValueError("name must not be empty")
        if not entity.state or entity.state.strip() == "":
            raise ValueError("state must not be empty")
        updated = await self.repo.update(entity)
        if updated is None:
            raise NotFoundError(f"City with id {entity.id} not found")
        return updated

    async def delete_city(self, id: int) -> None:
        deleted = await self.repo.delete(id)
        if not deleted:
            raise NotFoundError(f"City with id {id} not found")

    async def search_by_name(self, name: str) -> List[CityEntity]:
        return await self.repo.search_by_name(name)

