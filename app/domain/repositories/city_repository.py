from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.city_entity import CityEntity

class CityRepository(ABC):

    @abstractmethod
    def create(self, entity: CityEntity) -> CityEntity:
        pass

    @abstractmethod
    def list_all(self, limit: Optional[int] = None, offset: Optional[int] = None) -> List[CityEntity]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[CityEntity]:
        pass

    @abstractmethod
    def update(self, entity: CityEntity) -> CityEntity:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass

    @abstractmethod
    def search_by_name(self, name: str) -> List[CityEntity]:
        pass

