from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.data.models.album_model import AlbumModel
from app.domain.entities.album_entity import AlbumEntity
from app.domain.repositories.album_repository import AlbumRepository


class AlbumRepositoryImpl(AlbumRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    def base_query(self):
        return select(AlbumModel).options(selectinload(AlbumModel.image_urls))

    async def create(self, entity: AlbumEntity) -> AlbumEntity:
        model = AlbumModel(
        point_turism_id=entity.point_turism_id,
        image_urls=entity.image_urls[:10]
    )
        self.db.add(model)
        await self.db.commit()
        await self.db.refresh(model)

        return AlbumEntity(
        id=model.id,
        point_turism_id=model.point_turism_id,
        image_urls=model.image_urls,
        created_at=model.created_at
    )


    async def list_all(self, limit: Optional[int] = None, offset: Optional[int] = None) -> List[AlbumEntity]:
        query = self.base_query()
        if offset:
            query = query.offset(offset)
        if limit:
            query = query.limit(limit)

        result = await self.db.execute(query)
        albums = result.unique().scalars().all()

        return [
            AlbumEntity(
                id=a.id,
                point_turism_id=a.point_turism_id,
                images=[img.url for img in a.images] if a.images else [],
                created_at=a.created_at
            )
            for a in albums
        ]

    async def get_by_id(self, id: int) -> Optional[AlbumEntity]:
        result = await self.db.execute(
            select(AlbumModel)
            .filter(AlbumModel.id == id)
            .options(selectinload(AlbumModel.images))
        )
        a = result.unique().scalar_one_or_none()
        if not a:
            return None
        return AlbumEntity(
            id=a.id,
            point_turism_id=a.point_turism_id,
            images=[img.url for img in a.images] if a.images else [],
            created_at=a.created_at
        )

    async def update(self, entity: AlbumEntity) -> Optional[AlbumEntity]:
        result = await self.db.execute(select(AlbumModel).filter(AlbumModel.id == entity.id))
        model = result.scalar_one_or_none()
        if not model:
            return None

        if entity.point_turism_id is not None:
            model.point_turism_id = entity.point_turism_id

        await self.db.commit()
        await self.db.refresh(model)

        return AlbumEntity(
            id=model.id,
            point_turism_id=model.point_turism_id,
            images=[img.url for img in model.images] if model.images else [],
            created_at=model.created_at
        )

    async def delete(self, id: int) -> bool:
        result = await self.db.execute(select(AlbumModel).filter(AlbumModel.id == id))
        model = result.scalar_one_or_none()
        if not model:
            return False
        await self.db.delete(model)
        await self.db.commit()
        return True

    async def add_image_to_album(self, album_id: int, image_id: int) -> bool:
        result = await self.db.execute(select(AlbumModel).filter(AlbumModel.id == album_id))
        model = result.scalar_one_or_none()
        if not model:
            return False
        await self.db.commit()
        return True

    async def remove_image_from_album(self, album_id: int, image_id: int) -> bool:
        result = await self.db.execute(select(AlbumModel).filter(AlbumModel.id == album_id))
        model = result.scalar_one_or_none()
        if not model:
            return False
        await self.db.commit()
        return True
