from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.point_turism_entity import PointTurismEntity


class PointTurismRepository(ABC):

    @abstractmethod
    async def create(self, entity: PointTurismEntity) -> PointTurismEntity:
        pass

    @abstractmethod
    async def list_all(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> List[PointTurismEntity]:
        pass

    @abstractmethod
    async def get_by_id(self, id: int) -> Optional[PointTurismEntity]:
        pass

    @abstractmethod
    async def update(self, entity: PointTurismEntity) -> PointTurismEntity:
        pass

    @abstractmethod
    async def delete(self, id: int) -> None:
        pass

    @abstractmethod
    async def search_by_name(self, name: str) -> List[PointTurismEntity]:
        pass

    @abstractmethod
    async def filter(
        self,
        category_id: Optional[int] = None,
        city_id: Optional[int] = None,
        min_review: Optional[float] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> List[PointTurismEntity]:
        pass
