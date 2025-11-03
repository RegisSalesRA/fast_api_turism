from typing import List, Optional
from abc import ABC, abstractmethod
from app.domain.entities.category_entity import CategoryEntity

class CategoryRepository(ABC):

    @abstractmethod
    async def base_query(self):
        pass

    @abstractmethod
    async def create(self, entity: CategoryEntity) -> CategoryEntity:
        pass

    @abstractmethod
    async def get_by_id(self, id: int) -> Optional[CategoryEntity]:
        pass

    @abstractmethod
    async def update(self, entity: CategoryEntity) -> Optional[CategoryEntity]:
        pass

    @abstractmethod
    async def delete(self, id: int) -> bool:
        pass

    @abstractmethod
    async def search_by_name(self, name: str) -> List[CategoryEntity]:
        pass
