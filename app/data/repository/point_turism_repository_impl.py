from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.data.models.point_turism_model import PointTurismModel
from app.domain.entities.point_turism_entity import PointTurismEntity
from app.domain.repositories.point_turism_repository import PointTurismRepository


class PointTurismRepositoryImpl(PointTurismRepository):

    def __init__(self, db: AsyncSession):
        self.db = db

    async def list_all(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> List[PointTurismEntity]:

        stmt = select(PointTurismModel)

        if offset is not None:
            stmt = stmt.offset(offset)
        if limit is not None:
            stmt = stmt.limit(limit)

        result = await self.db.execute(stmt)
        points = result.scalars().all()

        return [self._to_entity(p) for p in points]

    async def get_by_id(self, point_id: int) -> Optional[PointTurismEntity]:
        stmt = select(PointTurismModel).where(PointTurismModel.id == point_id)
        result = await self.db.execute(stmt)
        model = result.scalars().first()

        return self._to_entity(model) if model else None

    async def create(self, entity: PointTurismEntity) -> PointTurismEntity:
        model = PointTurismModel(**entity.__dict__)

        self.db.add(model)
        await self.db.commit()
        await self.db.refresh(model)

        return self._to_entity(model)

    async def update(self, entity: PointTurismEntity) -> Optional[PointTurismEntity]:
        model = await self.get_model_by_id(entity.id)
        if not model:
            return None

        for field, value in entity.__dict__.items():
            if value is not None:
                setattr(model, field, value)

        await self.db.commit()
        await self.db.refresh(model)
        return self._to_entity(model)

    async def delete(self, point_id: int) -> bool:
        model = await self.get_model_by_id(point_id)
        if not model:
            return False

        await self.db.delete(model)
        await self.db.commit()
        return True

    async def search_by_name(self, name: str) -> List[PointTurismEntity]:
        stmt = select(PointTurismModel).where(
            PointTurismModel.name.ilike(f"%{name}%")
        )

        result = await self.db.execute(stmt)
        return [self._to_entity(p) for p in result.scalars().all()]

    async def filter(
        self,
        category_id: Optional[int] = None,
        city_id: Optional[int] = None,
        min_review: Optional[float] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> List[PointTurismEntity]:

        stmt = select(PointTurismModel)

        if category_id:
            stmt = stmt.where(PointTurismModel.category_id == category_id)
        if city_id:
            stmt = stmt.where(PointTurismModel.city_id == city_id)
        if min_review:
            stmt = stmt.where(PointTurismModel.review >= min_review)
        if offset:
            stmt = stmt.offset(offset)
        if limit:
            stmt = stmt.limit(limit)

        result = await self.db.execute(stmt)
        return [self._to_entity(p) for p in result.scalars().all()]

    async def get_model_by_id(self, point_id: int) -> Optional[PointTurismModel]:
        stmt = select(PointTurismModel).where(PointTurismModel.id == point_id)
        result = await self.db.execute(stmt)
        return result.scalars().first()

    def _to_entity(self, model: PointTurismModel) -> PointTurismEntity:
        return PointTurismEntity(
            id=model.id,
            name=model.name,
            images=model.image,
            description=model.description,
            category_id=model.category_id,
            city_id=model.city_id,
            review=model.review,
        )
