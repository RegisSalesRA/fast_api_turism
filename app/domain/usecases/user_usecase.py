from typing import Optional
from app.core.exceptions.domain_exceptions import NotFoundError
from app.core.pagination.paginator import Paginator
from app.core.pagination.schemas import PageParams
from app.domain.entities.user_entity import UserEntity
from app.domain.repositories.user_repository import UserRepository


class UserUseCase:

    def __init__(self, repository: UserRepository, paginator: Paginator):
        self.repo = repository
        self.paginator = paginator

    async def create_user(self, entity: UserEntity) -> UserEntity:
        if not entity.name or entity.name.strip() == "":
            raise ValueError("name must not be empty")
        if not entity.email or entity.email.strip() == "":
            raise ValueError("email must not be empty")
        
        # Check if user already exists
        existing = await self.repo.get_by_email(entity.email)
        if existing:
            raise ValueError(f"User with email {entity.email} already exists")
        
        created = await self.repo.create(entity)
        return created

    async def list_users(self, page_params: PageParams):
        query = self.repo.base_query()  
        return await self.paginator.paginate(query, page_params, UserEntity)

    async def get_user(self, id: str) -> UserEntity:
        u = await self.repo.get_by_id(id)
        if u is None:
            raise NotFoundError(f"User with id {id} not found")
        return u

    async def get_user_by_email(self, email: str) -> UserEntity:
        u = await self.repo.get_by_email(email)
        if u is None:
            raise NotFoundError(f"User with email {email} not found")
        return u

    async def update_user(self, entity: UserEntity) -> UserEntity:
        existing = await self.repo.get_by_id(entity.id)
        if existing is None:
            raise NotFoundError(f"User with id {entity.id} not found")

        return await self.repo.update(entity)

    async def delete_user(self, id: str) -> None:
        existing = await self.repo.get_by_id(id)
        if existing is None:
            raise NotFoundError(f"User with id {id} not found")

        await self.repo.delete(id)
