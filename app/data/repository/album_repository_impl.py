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
        model = AlbumModel(
            point_turism_id=entity.point_turism_id,
            image_urls=entity.image_urls[:10] if entity.image_urls else []
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
        albums = result.scalars().all()

        return [
            AlbumEntity(
                id=a.id,
                point_turism_id=a.point_turism_id,
                image_urls=a.image_urls,
                created_at=a.created_at
            )
            for a in albums
        ]

    async def get_by_id(self, id: int) -> Optional[AlbumEntity]:
        result = await self.db.execute(
            select(AlbumModel).filter(AlbumModel.id == id)
        )
        a = result.scalar_one_or_none()
        if not a:
            return None
        return AlbumEntity(
            id=a.id,
            point_turism_id=a.point_turism_id,
            image_urls=a.image_urls,
            created_at=a.created_at
        )

    async def update(self, entity: AlbumEntity) -> Optional[AlbumEntity]:
        result = await self.db.execute(select(AlbumModel).filter(AlbumModel.id == entity.id))
        model = result.scalar_one_or_none()
        if not model:
            return None

        if entity.point_turism_id is not None:
            model.point_turism_id = entity.point_turism_id
        
        if entity.image_urls is not None:
            model.image_urls = entity.image_urls[:10]

        await self.db.commit()
        await self.db.refresh(model)

        return AlbumEntity(
            id=model.id,
            point_turism_id=model.point_turism_id,
            image_urls=model.image_urls,
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

    async def add_image_to_album(self, album_id: int, image_url: str) -> bool:
        result = await self.db.execute(select(AlbumModel).filter(AlbumModel.id == album_id))
        model = result.scalar_one_or_none()
        if not model:
            return False
        
        if len(model.image_urls) < 10:
            # We need to make a copy to trigger SQLAlchemy change detection if it's not tracking mutations
            current_urls = list(model.image_urls)
            current_urls.append(image_url)
            model.image_urls = current_urls
            await self.db.commit()
            return True
        return False

    async def remove_image_from_album(self, album_id: int, image_url: str) -> bool:
        result = await self.db.execute(select(AlbumModel).filter(AlbumModel.id == album_id))
        model = result.scalar_one_or_none()
        if not model:
            return False
        
        if image_url in model.image_urls:
            current_urls = list(model.image_urls)
            current_urls.remove(image_url)
            model.image_urls = current_urls
            await self.db.commit()
            return True
        return False
