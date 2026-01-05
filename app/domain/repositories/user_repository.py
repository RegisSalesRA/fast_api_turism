from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.user_entity import UserEntity


class UserRepository(ABC):

    @abstractmethod
    async def create(self, entity: UserEntity) -> UserEntity:
        pass

    @abstractmethod
    async def list_all(self, limit: Optional[int] = None, offset: Optional[int] = None) -> List[UserEntity]:
        pass

    @abstractmethod
    async def get_by_id(self, id: str) -> Optional[UserEntity]:
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> Optional[UserEntity]:
        pass

    @abstractmethod
    async def update(self, entity: UserEntity) -> Optional[UserEntity]:
        pass

    @abstractmethod
    async def delete(self, id: str) -> bool:
        pass
