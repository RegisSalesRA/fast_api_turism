from typing import List, Optional
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
        
        # Check if user already reviewed this point
        existing = await self.repo.get_by_user_and_point(entity.user_id, entity.point_turism_id)
        if existing:
            raise ValueError("User already reviewed this point turism")

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

    async def update_my_review(self, user_id: str, point_turism_id: int, rating: Optional[float], comment: Optional[str]) -> ReviewEntity:
        existing = await self.repo.get_by_user_and_point(user_id, point_turism_id)
        if existing is None:
            raise NotFoundError(f"Review not found for this point turism")
        
        if rating is not None:
            if rating < 0 or rating > 5:
                raise ValueError("rating must be between 0 and 5")
            existing.rating = rating
            
        if comment is not None:
            existing.comment = comment

        return await self.repo.update(existing)

    async def delete_my_review(self, user_id: str, point_turism_id: int) -> None:
        existing = await self.repo.get_by_user_and_point(user_id, point_turism_id)
        if existing is None:
            raise NotFoundError(f"Review not found for this point turism")

        await self.repo.delete(existing.id)

