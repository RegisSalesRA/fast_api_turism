from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.data.models.category_model import CategoryModel
from app.domain.entities.category_entity import CategoryEntity
from app.domain.repositories.category_repository import CategoryRepository


class CategoryRepositoryImpl(CategoryRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    def base_query(self): 
        return select(CategoryModel)

    async def list_all(self, limit: int = 10, offset: int = 0) -> List[CategoryEntity]:
        result = await self.db.execute(
            select(CategoryModel).offset(offset).limit(limit)
        )
        models = result.scalars().all()
        return [CategoryEntity(id=m.id, name=m.name) for m in models]

    async def get_by_id(self, category_id: int) -> Optional[CategoryEntity]:
        result = await self.db.execute(
            select(CategoryModel).where(CategoryModel.id == category_id)
        )
        model = result.scalar_one_or_none()
        if not model:
            return None
        return CategoryEntity(id=model.id, name=model.name)

    async def create(self, entity: CategoryEntity) -> CategoryEntity:
        model = CategoryModel(name=entity.name)
        self.db.add(model)
        await self.db.commit()
        await self.db.refresh(model)
        return CategoryEntity(id=model.id, name=model.name)

    async def update(self, entity: CategoryEntity) -> Optional[CategoryEntity]:
        result = await self.db.execute(
            select(CategoryModel).where(CategoryModel.id == entity.id)
        )
        model = result.scalar_one_or_none()
        if not model:
            return None

        model.name = entity.name or model.name
        await self.db.commit()
        await self.db.refresh(model)

        return CategoryEntity(id=model.id, name=model.name)

    async def delete(self, category_id: int) -> bool:
        result = await self.db.execute(
            select(CategoryModel).where(CategoryModel.id == category_id)
        )
        model = result.scalar_one_or_none()
        if not model:
            return False

        await self.db.delete(model)
        await self.db.commit()
        return True

    async def search_by_name(self, name: str) -> List[CategoryEntity]:
        result = await self.db.execute(
            select(CategoryModel).where(CategoryModel.name.ilike(f"%{name}%"))
        )
        models = result.scalars().all()
        return [CategoryEntity(id=m.id, name=m.name) for m in models]
