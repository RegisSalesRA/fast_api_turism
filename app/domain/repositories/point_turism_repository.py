from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.point_turism_entity import PointTurismEntity

class PointTurismRepository(ABC):

    @abstractmethod
    def create(self, entity: PointTurismEntity) -> PointTurismEntity:
        pass

    @abstractmethod
    def list_all(self, limit: Optional[int] = None, offset: Optional[int] = None) -> List[PointTurismEntity]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[PointTurismEntity]:
        pass

    @abstractmethod
    def update(self, entity: PointTurismEntity) -> PointTurismEntity:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass

    @abstractmethod
    def search_by_name(self, name: str) -> List[PointTurismEntity]:
        pass

    @abstractmethod
    def filter(self, city_id: Optional[int] = None, category_id: Optional[int] = None,
               min_review: Optional[float] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> List[PointTurismEntity]:
        pass

    @abstractmethod
    def summary_by_city(self):
        """Retorna agregações por cidade — forma livre (lista de dicts)"""
        pass
