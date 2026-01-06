from app.core.exceptions.domain_exceptions import NotFoundError
from app.core.pagination.paginator import Paginator
from app.core.pagination.schemas import PageParams
from app.domain.entities.image_entity import ImageEntity
from app.domain.repositories.image_repository import ImageRepository
from app.domain.repositories.point_turism_repository import PointTurismRepository


class ImageUseCase:

    def __init__(self, repository: ImageRepository, paginator: Paginator, point_turism_repo: PointTurismRepository = None):
        self.repo = repository
        self.paginator = paginator
        self.point_turism_repo = point_turism_repo

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

    async def associate_image_to_point_turism(self, image_id: int, point_turism_id: int) -> None:
        """Associar uma imagem a um ponto turístico"""
        # Verificar se a imagem existe
        image = await self.repo.get_by_id(image_id)
        if image is None:
            raise NotFoundError(f"Image with id {image_id} not found")
        
        # Verificar se o ponto turístico existe
        if self.point_turism_repo:
            point_turism = await self.point_turism_repo.get_by_id(point_turism_id)
            if point_turism is None:
                raise NotFoundError(f"Point turism with id {point_turism_id} not found")
        
        # Associar a imagem ao ponto turístico
        await self.repo.associate_image_to_point_turism(image_id, point_turism_id)

