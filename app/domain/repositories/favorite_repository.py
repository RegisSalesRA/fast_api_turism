from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.favorite_entity import FavoriteEntity


class FavoriteRepository(ABC):

    @abstractmethod
    async def create(self, entity: FavoriteEntity) -> FavoriteEntity:
        pass

    @abstractmethod
    async def list_all(self, limit: int = None, offset: int = None) -> List[FavoriteEntity]:
        pass

    @abstractmethod
    async def get_by_user(self, user_id: str) -> List[FavoriteEntity]:
        pass

    @abstractmethod
    async def get_by_user_and_point(self, user_id: str, point_turism_id: int) -> FavoriteEntity:
        pass

    @abstractmethod
    async def delete(self, user_id: str, point_turism_id: int) -> bool:
        pass

    @abstractmethod
    async def is_favorite(self, user_id: str, point_turism_id: int) -> bool:
        pass
