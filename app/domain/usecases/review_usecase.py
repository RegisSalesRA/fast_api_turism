from typing import List
from app.core.exceptions.domain_exceptions import NotFoundError
from app.core.pagination.paginator import Paginator
from app.core.pagination.schemas import PageParams
from app.domain.entities.review_entity import ReviewEntity
from app.domain.repositories.review_repository import ReviewRepository


class ReviewUseCase:

    def __init__(self, repository: ReviewRepository, paginator: Paginator):
        self.repo = repository
        self.paginator = paginator

    async def create_review(self, entity: ReviewEntity) -> ReviewEntity:
        if entity.rating < 0 or entity.rating > 5:
            raise ValueError("rating must be between 0 and 5")
        if not entity.user_id:
            raise ValueError("user_id must not be empty")
        if not entity.point_turism_id:
            raise ValueError("point_turism_id must not be empty")
        
        created = await self.repo.create(entity)
        return created

    async def list_reviews(self, page_params: PageParams):
        query = self.repo.base_query()  
        return await self.paginator.paginate(query, page_params, ReviewEntity)

    async def get_review(self, id: int) -> ReviewEntity:
        r = await self.repo.get_by_id(id)
        if r is None:
            raise NotFoundError(f"Review with id {id} not found")
        return r

    async def get_reviews_by_point_turism(self, point_turism_id: int) -> List[ReviewEntity]:
        return await self.repo.get_by_point_turism(point_turism_id)

    async def get_reviews_by_user(self, user_id: str) -> List[ReviewEntity]:
        return await self.repo.get_by_user(user_id)

    async def update_review(self, entity: ReviewEntity) -> ReviewEntity:
        existing = await self.repo.get_by_id(entity.id)
        if existing is None:
            raise NotFoundError(f"Review with id {entity.id} not found")
        
        if entity.rating < 0 or entity.rating > 5:
            raise ValueError("rating must be between 0 and 5")

        return await self.repo.update(entity)

    async def delete_review(self, id: int) -> None:
        existing = await self.repo.get_by_id(id)
        if existing is None:
            raise NotFoundError(f"Review with id {id} not found")

        await self.repo.delete(id)
