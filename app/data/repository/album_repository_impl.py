from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.data.models.album_model import AlbumModel
from app.domain.entities.album_entity import AlbumEntity
from app.domain.repositories.album_repository import AlbumRepository


class AlbumRepositoryImpl(AlbumRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    def base_query(self):
        return select(AlbumModel)

    async def create(self, entity: AlbumEntity) -> AlbumEntity:
        model = AlbumModel()
        self.db.add(model)
        await self.db.commit()
        await self.db.refresh(model)

        return AlbumEntity(
            id=model.id,
            images=[],
        )

    async def list_all(self, limit: Optional[int] = None, offset: Optional[int] = None) -> List[AlbumEntity]:
        query = self.base_query()
        if offset:
            query = query.offset(offset)
        if limit:
            query = query.limit(limit)

        result = await self.db.execute(query)
        albums = result.scalars().all()

        return [
            AlbumEntity(
                id=a.id,
                images=[],
            )
            for a in albums
        ]

    async def get_by_id(self, id: int) -> Optional[AlbumEntity]:
        result = await self.db.execute(select(AlbumModel).filter(AlbumModel.id == id))
        a = result.scalar_one_or_none()
        if not a:
            return None
        return AlbumEntity(
            id=a.id,
            images=[],
        )

    async def update(self, entity: AlbumEntity) -> Optional[AlbumEntity]:
        result = await self.db.execute(select(AlbumModel).filter(AlbumModel.id == entity.id))
        model = result.scalar_one_or_none()
        if not model:
            return None

        await self.db.commit()
        await self.db.refresh(model)

        return AlbumEntity(
            id=model.id,
            images=[],
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
