from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.album_entity import AlbumEntity


class AlbumRepository(ABC):

    @abstractmethod
    async def create(self, entity: AlbumEntity) -> AlbumEntity:
        pass

    @abstractmethod
    async def list_all(self, limit: Optional[int] = None, offset: Optional[int] = None) -> List[AlbumEntity]:
        pass

    @abstractmethod
    async def get_by_id(self, id: int) -> Optional[AlbumEntity]:
        pass

    @abstractmethod
    async def update(self, entity: AlbumEntity) -> Optional[AlbumEntity]:
        pass

    @abstractmethod
    async def delete(self, id: int) -> bool:
        pass

    @abstractmethod
    async def add_image_to_album(self, album_id: int, image_url: str) -> bool:
        pass

    @abstractmethod
    async def remove_image_from_album(self, album_id: int, image_url: str) -> bool:
        pass
