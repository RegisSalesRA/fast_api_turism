from app.core.exceptions.domain_exceptions import NotFoundError
from app.core.pagination.paginator import Paginator
from app.core.pagination.schemas import PageParams
from app.domain.entities.image_entity import ImageEntity
from app.domain.repositories.image_repository import ImageRepository


class ImageUseCase:

    def __init__(self, repository: ImageRepository, paginator: Paginator):
        self.repo = repository
        self.paginator = paginator

    async def create_image(self, entity: ImageEntity) -> ImageEntity:
        if not entity.url or entity.url.strip() == "":
            raise ValueError("url must not be empty")
        
        created = await self.repo.create(entity)
        return created

    async def list_images(self, page_params: PageParams):
        query = self.repo.base_query()  
        return await self.paginator.paginate(query, page_params, ImageEntity)

    async def get_image(self, id: int) -> ImageEntity:
        i = await self.repo.get_by_id(id)
        if i is None:
            raise NotFoundError(f"Image with id {id} not found")
        return i

    async def update_image(self, entity: ImageEntity) -> ImageEntity:
        existing = await self.repo.get_by_id(entity.id)
        if existing is None:
            raise NotFoundError(f"Image with id {entity.id} not found")
        
        if not entity.url or entity.url.strip() == "":
            raise ValueError("url must not be empty")

        return await self.repo.update(entity)

    async def delete_image(self, id: int) -> None:
        existing = await self.repo.get_by_id(id)
        if existing is None:
            raise NotFoundError(f"Image with id {id} not found")

        await self.repo.delete(id)
