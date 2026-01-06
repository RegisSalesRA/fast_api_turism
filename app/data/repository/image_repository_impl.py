from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.data.models.image_model import ImageModel
from app.domain.entities.image_entity import ImageEntity
from app.domain.repositories.image_repository import ImageRepository


class ImageRepositoryImpl(ImageRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    def base_query(self):
        return select(ImageModel)

    async def create(self, entity: ImageEntity) -> ImageEntity:
        model = ImageModel(
            url=entity.url,
            point_turism_id=entity.point_turism_id,
        )
        self.db.add(model)
        await self.db.commit()
        await self.db.refresh(model)

        return ImageEntity(
            id=model.id,
            url=model.url,
            point_turism_id=model.point_turism_id,
        )

    async def list_all(self, limit: Optional[int] = None, offset: Optional[int] = None) -> List[ImageEntity]:
        query = self.base_query()
        if offset:
            query = query.offset(offset)
        if limit:
            query = query.limit(limit)

        result = await self.db.execute(query)
        images = result.scalars().all()

        return [
            ImageEntity(
                id=i.id,
                url=i.url,
                point_turism_id=i.point_turism_id,
            )
            for i in images
        ]

    async def get_by_id(self, id: int) -> Optional[ImageEntity]:
        result = await self.db.execute(select(ImageModel).filter(ImageModel.id == id))
        i = result.scalar_one_or_none()
        if not i:
            return None
        return ImageEntity(
            id=i.id,
            url=i.url,
            point_turism_id=i.point_turism_id,
        )

    async def update(self, entity: ImageEntity) -> Optional[ImageEntity]:
        result = await self.db.execute(select(ImageModel).filter(ImageModel.id == entity.id))
        model = result.scalar_one_or_none()
        if not model:
            return None

        model.url = entity.url or model.url
        model.point_turism_id = entity.point_turism_id if entity.point_turism_id is not None else model.point_turism_id

        await self.db.commit()
        await self.db.refresh(model)

        return ImageEntity(
            id=model.id,
            url=model.url,
            point_turism_id=model.point_turism_id,
        )

    async def delete(self, id: int) -> bool:
        result = await self.db.execute(select(ImageModel).filter(ImageModel.id == id))
        model = result.scalar_one_or_none()
        if not model:
            return False
        await self.db.delete(model)
        await self.db.commit()
        return True

    async def associate_image_to_point_turism(self, image_id: int, point_turism_id: int) -> None:
        """Associar uma imagem a um ponto turístico - DEPRECATED"""
        pass
