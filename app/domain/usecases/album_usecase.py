from app.core.exceptions.domain_exceptions import NotFoundError
from app.core.pagination.paginator import Paginator
from app.core.pagination.schemas import PageParams
from app.domain.entities.album_entity import AlbumEntity
from app.domain.repositories.album_repository import AlbumRepository


class AlbumUseCase:

    def __init__(self, repository: AlbumRepository, paginator: Paginator):
        self.repo = repository
        self.paginator = paginator

    async def create_album(self, entity: AlbumEntity) -> AlbumEntity:
        created = await self.repo.create(entity)
        return created

    async def list_albums(self, page_params: PageParams):
        query = self.repo.base_query()  
        return await self.paginator.paginate(query, page_params, AlbumEntity)

    async def get_album(self, id: int) -> AlbumEntity:
        a = await self.repo.get_by_id(id)
        if a is None:
            raise NotFoundError(f"Album with id {id} not found")
        return a

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

    async def add_image_to_album(self, album_id: int, image_id: int) -> bool:
        existing = await self.repo.get_by_id(album_id)
        if existing is None:
            raise NotFoundError(f"Album with id {album_id} not found")
        
        return await self.repo.add_image_to_album(album_id, image_id)

    async def remove_image_from_album(self, album_id: int, image_id: int) -> bool:
        existing = await self.repo.get_by_id(album_id)
        if existing is None:
            raise NotFoundError(f"Album with id {album_id} not found")
        
        return await self.repo.remove_image_from_album(album_id, image_id)
