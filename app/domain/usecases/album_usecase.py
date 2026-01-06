from typing import List, Optional
from app.core.exceptions.domain_exceptions import NotFoundError
from app.core.pagination.paginator import Paginator, PageParams
from app.domain.entities.album_entity import AlbumEntity
from app.domain.repositories.album_repository import AlbumRepository


class AlbumUseCase:
    def __init__(self, repository: AlbumRepository, paginator: Paginator):
        self.repo = repository
        self.paginator = paginator

    async def create_album(self, entity: AlbumEntity) -> AlbumEntity:
        return await self.repo.create(entity)

    async def list_albums(self, page_params: PageParams):
        query = self.repo.base_query()
        return await self.paginator.paginate(query, page_params, AlbumEntity)

    async def get_album(self, id: int) -> AlbumEntity:
        album = await self.repo.get_by_id(id)
        if album is None:
            raise NotFoundError(f"Album with id {id} not found")
        return album

    async def update_album(self, entity: AlbumEntity) -> AlbumEntity:
        existing = await self.repo.get_by_id(entity.id)
        if existing is None:
            raise NotFoundError(f"Album with id {entity.id} not found")
        return await self.repo.update(entity)

    async def delete_album(self, id: int) -> None:
        existing = await self.repo.get_by_id(id)
        if existing is None:
            raise NotFoundError(f"Album with id {id} not found")
        await self.repo.delete(id)

    async def add_image_to_album(self, album_id: int, image_url: str) -> None:
        success = await self.repo.add_image_to_album(album_id, image_url)
        if not success:
            raise NotFoundError(f"Album with id {album_id} not found or limit reached")

    async def remove_image_from_album(self, album_id: int, image_url: str) -> None:
        success = await self.repo.remove_image_from_album(album_id, image_url)
        if not success:
            raise NotFoundError(f"Album with id {album_id} not found or image not in album")
