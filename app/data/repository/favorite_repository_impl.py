from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.data.models.favorite_model import FavoriteModel
from app.domain.entities.favorite_entity import FavoriteEntity
from app.domain.repositories.favorite_repository import FavoriteRepository


class FavoriteRepositoryImpl(FavoriteRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, entity: FavoriteEntity) -> FavoriteEntity:
        model = FavoriteModel(
            user_id=entity.user_id,
            point_turism_id=entity.point_turism_id,
        )
        self.db.add(model)
        await self.db.commit()
        await self.db.refresh(model)

        return FavoriteEntity(
            user_id=model.user_id,
            point_turism_id=model.point_turism_id,
            created_at=model.created_at,
        )

    async def list_all(self, limit: int = None, offset: int = None) -> List[FavoriteEntity]:
        query = select(FavoriteModel)
        if offset:
            query = query.offset(offset)
        if limit:
            query = query.limit(limit)

        result = await self.db.execute(query)
        favorites = result.scalars().all()

        return [
            FavoriteEntity(
                user_id=f.user_id,
                point_turism_id=f.point_turism_id,
                created_at=f.created_at,
            )
            for f in favorites
        ]

    async def get_by_user(self, user_id: str) -> List[FavoriteEntity]:
        result = await self.db.execute(
            select(FavoriteModel).filter(FavoriteModel.user_id == user_id)
        )
        favorites = result.scalars().all()

        return [
            FavoriteEntity(
                user_id=f.user_id,
                point_turism_id=f.point_turism_id,
                created_at=f.created_at,
            )
            for f in favorites
        ]

    async def get_by_user_and_point(self, user_id: str, point_turism_id: int) -> Optional[FavoriteEntity]:
        result = await self.db.execute(
            select(FavoriteModel).filter(
                FavoriteModel.user_id == user_id,
                FavoriteModel.point_turism_id == point_turism_id
            )
        )
        f = result.scalar_one_or_none()
        if not f:
            return None
        return FavoriteEntity(
            user_id=f.user_id,
            point_turism_id=f.point_turism_id,
            created_at=f.created_at,
        )

    async def delete(self, user_id: str, point_turism_id: int) -> bool:
        result = await self.db.execute(
            select(FavoriteModel).filter(
                FavoriteModel.user_id == user_id,
                FavoriteModel.point_turism_id == point_turism_id
            )
        )
        model = result.scalar_one_or_none()
        if not model:
            return False
        await self.db.delete(model)
        await self.db.commit()
        return True

    async def is_favorite(self, user_id: str, point_turism_id: int) -> bool:
        result = await self.db.execute(
            select(FavoriteModel).filter(
                FavoriteModel.user_id == user_id,
                FavoriteModel.point_turism_id == point_turism_id
            )
        )
        return result.scalar_one_or_none() is not None
