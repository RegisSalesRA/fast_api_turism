from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.city_entity import CityEntity

class CityRepository(ABC):

    @abstractmethod
    async def create(self, entity: CityEntity) -> CityEntity:
        pass

    @abstractmethod
    async def list_all(self, limit: Optional[int] = None, offset: Optional[int] = None) -> List[CityEntity]:
        pass

    @abstractmethod
    async def get_by_id(self, id: int) -> Optional[CityEntity]:
        pass

    @abstractmethod
    async def update(self, entity: CityEntity) -> CityEntity:
        pass

    @abstractmethod
    async def delete(self, id: int) -> None:
        pass

    @abstractmethod
    async def search_by_name(self, name: str) -> List[CityEntity]:
        pass

