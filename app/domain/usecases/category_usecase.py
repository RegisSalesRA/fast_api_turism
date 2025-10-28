from typing import List, Optional
from app.core.exceptions.domain_exceptions import NotFoundError
from app.domain.entities.category_entity import CategoryEntity
from app.domain.repositories.category_repository import CategoryRepository 
 
class CategoryUseCase: 

    def __init__(self, repository: CategoryRepository):
        self.repo = repository

    def create_category(self, entity: CategoryEntity) -> CategoryEntity:
        if not entity.name or entity.name.strip() == "":
            raise ValueError("name must not be empty")
        created = self.repo.create(entity)
        return created

    def list_categorys(self, *, limit: Optional[int] = None, offset: Optional[int] = None) -> List[CategoryEntity]:
        return self.repo.list_all(limit=limit, offset=offset)

    def get_category(self, id: int) -> CategoryEntity:
        p = self.repo.get_by_id(id)
        if p is None:
            raise NotFoundError(f"Category with id {id} not found")
        return p

    def update_category(self, entity: CategoryEntity) -> CategoryEntity:
        existing = self.repo.get_by_id(entity.id)
        if existing is None:
            raise NotFoundError(f"Category with id {entity.id} not found")

        return self.repo.update(entity)
 

    def delete_category(self, id: int) -> None:
        existing = self.repo.get_by_id(id)
        if existing is None:
            raise NotFoundError(f"Category with id {id} not found")
        self.repo.delete(id)

    def search_by_name(self, name: str) -> List[CategoryEntity]:
        if not name:
            return []
        return self.repo.search_by_name(name)
