from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.category_entity import CategoryEntity 

class CategoryRepository(ABC):

    @abstractmethod
    def create(self, entity: CategoryEntity) -> CategoryEntity:
        pass

    @abstractmethod
    def list_all(self, limit: Optional[int] = None, offset: Optional[int] = None) -> List[CategoryEntity]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[CategoryEntity]:
        pass

    @abstractmethod
    def update(self, entity: CategoryEntity) -> CategoryEntity:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass

    @abstractmethod
    def search_by_name(self, name: str) -> List[CategoryEntity]:
        pass