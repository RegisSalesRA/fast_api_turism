from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.review_entity import ReviewEntity


class ReviewRepository(ABC):

    @abstractmethod
    def base_query(self):
        pass

    @abstractmethod
    async def create(self, entity: ReviewEntity) -> ReviewEntity:
        pass

    @abstractmethod
    async def list_all(self, limit: Optional[int] = None, offset: Optional[int] = None) -> List[ReviewEntity]:
        pass

    @abstractmethod
    async def get_by_id(self, id: int) -> Optional[ReviewEntity]:
        pass

    @abstractmethod
    async def get_by_user_and_point(self, user_id: str, point_turism_id: int) -> Optional[ReviewEntity]:
        pass

    @abstractmethod
    async def get_by_point_turism(self, point_turism_id: int) -> List[ReviewEntity]:
        pass

    @abstractmethod
    async def get_by_user(self, user_id: str) -> List[ReviewEntity]:
        pass

    @abstractmethod
    async def update(self, entity: ReviewEntity) -> Optional[ReviewEntity]:
        pass

    @abstractmethod
    async def delete(self, id: int) -> bool:
        pass
