from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.data.models.user_model import UserModel
from app.domain.entities.user_entity import UserEntity
from app.domain.repositories.user_repository import UserRepository


class UserRepositoryImpl(UserRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    def base_query(self):
        return select(UserModel)

    async def create(self, entity: UserEntity) -> UserEntity:
        model = UserModel(
            id=entity.id,
            name=entity.name,
            email=entity.email,
            role=entity.role,
        )
        self.db.add(model)
        await self.db.commit()
        await self.db.refresh(model)

        return UserEntity(
            id=model.id,
            name=model.name,
            email=model.email,
            role=model.role,
            created_at=model.created_at,
            last_login=model.last_login,
        )

    async def list_all(self, limit: Optional[int] = None, offset: Optional[int] = None) -> List[UserEntity]:
        query = self.base_query()
        if offset:
            query = query.offset(offset)
        if limit:
            query = query.limit(limit)

        result = await self.db.execute(query)
        users = result.scalars().all()

        return [
            UserEntity(
                id=u.id,
                name=u.name,
                email=u.email,
                role=u.role,
                created_at=u.created_at,
                last_login=u.last_login,
            )
            for u in users
        ]

    async def get_by_id(self, id: str) -> Optional[UserEntity]:
        result = await self.db.execute(select(UserModel).filter(UserModel.id == id))
        u = result.scalar_one_or_none()
        if not u:
            return None
        return UserEntity(
            id=u.id,
            name=u.name,
            email=u.email,
            role=u.role,
            created_at=u.created_at,
            last_login=u.last_login,
        )

    async def get_by_email(self, email: str) -> Optional[UserEntity]:
        result = await self.db.execute(select(UserModel).filter(UserModel.email == email))
        u = result.scalar_one_or_none()
        if not u:
            return None
        return UserEntity(
            id=u.id,
            name=u.name,
            email=u.email,
            role=u.role,
            created_at=u.created_at,
            last_login=u.last_login,
        )

    async def update(self, entity: UserEntity) -> Optional[UserEntity]:
        result = await self.db.execute(select(UserModel).filter(UserModel.id == entity.id))
        model = result.scalar_one_or_none()
        if not model:
            return None

        model.name = entity.name or model.name
        model.email = entity.email or model.email
        model.role = entity.role or model.role
        model.last_login = entity.last_login or model.last_login

        await self.db.commit()
        await self.db.refresh(model)

        return UserEntity(
            id=model.id,
            name=model.name,
            email=model.email,
            role=model.role,
            created_at=model.created_at,
            last_login=model.last_login,
        )

    async def delete(self, id: str) -> bool:
        result = await self.db.execute(select(UserModel).filter(UserModel.id == id))
        model = result.scalar_one_or_none()
        if not model:
            return False
        await self.db.delete(model)
        await self.db.commit()
        return True
