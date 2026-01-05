from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.image_entity import ImageEntity


class ImageRepository(ABC):

    @abstractmethod
    async def create(self, entity: ImageEntity) -> ImageEntity:
        pass

    @abstractmethod
    async def list_all(self, limit: Optional[int] = None, offset: Optional[int] = None) -> List[ImageEntity]:
        pass

    @abstractmethod
    async def get_by_id(self, id: int) -> Optional[ImageEntity]:
        pass

    @abstractmethod
    async def update(self, entity: ImageEntity) -> Optional[ImageEntity]:
        pass

    @abstractmethod
    async def delete(self, id: int) -> bool:
        pass
