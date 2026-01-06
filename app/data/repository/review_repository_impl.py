from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.data.models.review_model import ReviewModel
from app.domain.entities.review_entity import ReviewEntity
from app.domain.repositories.review_repository import ReviewRepository


class ReviewRepositoryImpl(ReviewRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    def base_query(self):
        return select(ReviewModel)

    async def create(self, entity: ReviewEntity) -> ReviewEntity:
        model = ReviewModel(
            user_id=entity.user_id,
            point_turism_id=entity.point_turism_id,
            rating=entity.rating,
            comment=entity.comment,
        )
        self.db.add(model)
        await self.db.commit()
        await self.db.refresh(model)

        return ReviewEntity(
            id=model.id,
            user_id=model.user_id,
            point_turism_id=model.point_turism_id,
            rating=model.rating,
            comment=model.comment,
            created_at=model.created_at,
        )

    async def list_all(self, limit: Optional[int] = None, offset: Optional[int] = None) -> List[ReviewEntity]:
        query = self.base_query()
        if offset:
            query = query.offset(offset)
        if limit:
            query = query.limit(limit)

        result = await self.db.execute(query)
        reviews = result.scalars().all()

        return [
            ReviewEntity(
                id=r.id,
                user_id=r.user_id,
                point_turism_id=r.point_turism_id,
                rating=r.rating,
                comment=r.comment,
                created_at=r.created_at,
            )
            for r in reviews
        ]

    async def get_by_id(self, id: int) -> Optional[ReviewEntity]:
        result = await self.db.execute(select(ReviewModel).filter(ReviewModel.id == id))
        r = result.scalar_one_or_none()
        if not r:
            return None
        return ReviewEntity(
            id=r.id,
            user_id=r.user_id,
            point_turism_id=r.point_turism_id,
            rating=r.rating,
            comment=r.comment,
            created_at=r.created_at,
        )

    async def get_by_user_and_point(self, user_id: str, point_turism_id: int) -> Optional[ReviewEntity]:
        result = await self.db.execute(
            select(ReviewModel).filter(
                ReviewModel.user_id == user_id,
                ReviewModel.point_turism_id == point_turism_id
            )
        )
        r = result.scalar_one_or_none()
        if not r:
            return None
        return ReviewEntity(
            id=r.id,
            user_id=r.user_id,
            point_turism_id=r.point_turism_id,
            rating=r.rating,
            comment=r.comment,
            created_at=r.created_at,
        )

    async def get_by_point_turism(self, point_turism_id: int) -> List[ReviewEntity]:
        result = await self.db.execute(
            select(ReviewModel).filter(ReviewModel.point_turism_id == point_turism_id)
        )
        reviews = result.scalars().all()

        return [
            ReviewEntity(
                id=r.id,
                user_id=r.user_id,
                point_turism_id=r.point_turism_id,
                rating=r.rating,
                comment=r.comment,
                created_at=r.created_at,
            )
            for r in reviews
        ]

    async def get_by_user(self, user_id: str) -> List[ReviewEntity]:
        result = await self.db.execute(select(ReviewModel).filter(ReviewModel.user_id == user_id))
        reviews = result.scalars().all()

        return [
            ReviewEntity(
                id=r.id,
                user_id=r.user_id,
                point_turism_id=r.point_turism_id,
                rating=r.rating,
                comment=r.comment,
                created_at=r.created_at,
            )
            for r in reviews
        ]

    async def update(self, entity: ReviewEntity) -> Optional[ReviewEntity]:
        result = await self.db.execute(select(ReviewModel).filter(ReviewModel.id == entity.id))
        model = result.scalar_one_or_none()
        if not model:
            return None

        model.rating = entity.rating if entity.rating is not None else model.rating
        model.comment = entity.comment if entity.comment is not None else model.comment

        await self.db.commit()
        await self.db.refresh(model)

        return ReviewEntity(
            id=model.id,
            user_id=model.user_id,
            point_turism_id=model.point_turism_id,
            rating=model.rating,
            comment=model.comment,
            created_at=model.created_at,
        )

    async def delete(self, id: int) -> bool:
        result = await self.db.execute(select(ReviewModel).filter(ReviewModel.id == id))
        model = result.scalar_one_or_none()
        if not model:
            return False
        await self.db.delete(model)
        await self.db.commit()
        return True
