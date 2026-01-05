from typing import List
from app.core.exceptions.domain_exceptions import NotFoundError
from app.domain.entities.favorite_entity import FavoriteEntity
from app.domain.repositories.favorite_repository import FavoriteRepository


class FavoriteUseCase:

    def __init__(self, repository: FavoriteRepository):
        self.repo = repository

    async def add_favorite(self, entity: FavoriteEntity) -> FavoriteEntity:
        if not entity.user_id:
            raise ValueError("user_id must not be empty")
        if not entity.point_turism_id:
            raise ValueError("point_turism_id must not be empty")
        
        # Check if already favorite
        existing = await self.repo.get_by_user_and_point(entity.user_id, entity.point_turism_id)
        if existing:
            raise ValueError(f"Point turism {entity.point_turism_id} is already in favorites for user {entity.user_id}")
        
        created = await self.repo.create(entity)
        return created

    async def list_favorites(self, limit: int = None, offset: int = None) -> List[FavoriteEntity]:
        return await self.repo.list_all(limit, offset)

    async def get_user_favorites(self, user_id: str) -> List[FavoriteEntity]:
        return await self.repo.get_by_user(user_id)

    async def is_favorite(self, user_id: str, point_turism_id: int) -> bool:
        return await self.repo.is_favorite(user_id, point_turism_id)

    async def remove_favorite(self, user_id: str, point_turism_id: int) -> None:
        existing = await self.repo.get_by_user_and_point(user_id, point_turism_id)
        if existing is None:
            raise NotFoundError(
                f"Favorite with user_id {user_id} and point_turism_id {point_turism_id} not found"
            )

        await self.repo.delete(user_id, point_turism_id)
