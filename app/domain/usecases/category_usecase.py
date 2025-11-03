from typing import List, Optional
from app.core.exceptions.domain_exceptions import NotFoundError
from app.core.pagination.paginator import Paginator, PageParams
from app.domain.entities.category_entity import CategoryEntity
from app.domain.repositories.category_repository import CategoryRepository


class CategoryUseCase:

    def __init__(self, repository: CategoryRepository, paginator: Paginator):
        self.repo = repository
        self.paginator = paginator

    async def create_category(self, entity: CategoryEntity) -> CategoryEntity:
        if not entity.name or entity.name.strip() == "":
            raise ValueError("name must not be empty")
        
        created = await self.repo.create(entity)
        return created

    async def list_categories(self, page_params: PageParams):
        query = self.repo.base_query()  
        return await self.paginator.paginate(query, page_params, CategoryEntity)

    async def get_category(self, id: int) -> CategoryEntity:
        p = await self.repo.get_by_id(id)
        if p is None:
            raise NotFoundError(f"Category with id {id} not found")
        return p

    async def update_category(self, entity: CategoryEntity) -> CategoryEntity:
        existing = await self.repo.get_by_id(entity.id)
        if existing is None:
            raise NotFoundError(f"Category with id {entity.id} not found")

        return await self.repo.update(entity)

    async def delete_category(self, id: int) -> None:
        existing = await self.repo.get_by_id(id)
        if existing is None:
            raise NotFoundError(f"Category with id {id} not found")

        await self.repo.delete(id)

    async def search_by_name(self, name: str) -> List[CategoryEntity]:
        if not name:
            return []
        return await self.repo.search_by_name(name)
