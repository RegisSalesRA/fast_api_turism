from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.data.models.city_model import CityModel
from app.domain.entities.city_entity import CityEntity
from app.domain.repositories.city_repository import CityRepository


class CityRepositoryImpl(CityRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    def base_query(self):
        return select(CityModel)

    async def list_all(self, limit: Optional[int] = None, offset: Optional[int] = None) -> List[CityEntity]:
        query = self.base_query()
        if offset:
            query = query.offset(offset)
        if limit:
            query = query.limit(limit)

        result = await self.db.execute(query)
        cities = result.scalars().all()

        return [
            CityEntity(
                id=c.id,
                name=c.name,
                state=c.state,
                country=c.country,
                description=c.description,
            )
            for c in cities
        ]

    async def get_by_id(self, city_id: int) -> Optional[CityEntity]:
        result = await self.db.execute(select(CityModel).filter(CityModel.id == city_id))
        c = result.scalar_one_or_none()
        if not c:
            return None
        return CityEntity(
            id=c.id,
            name=c.name,
            state=c.state,
            country=c.country,
            description=c.description,
        )

    async def create(self, city: CityEntity) -> CityEntity:
        model = CityModel(
            name=city.name,
            state=city.state,
            country=city.country,
            description=city.description,
        )
        self.db.add(model)
        await self.db.commit()
        await self.db.refresh(model)

        return CityEntity(
            id=model.id,
            name=model.name,
            state=model.state,
            country=model.country,
            description=model.description,
        )

    async def update(self, entity: CityEntity) -> Optional[CityEntity]:
        result = await self.db.execute(select(CityModel).filter(CityModel.id == entity.id))
        model = result.scalar_one_or_none()
        if not model:
            return None

        model.name = entity.name or model.name
        model.state = entity.state or model.state
        model.country = entity.country or model.country
        model.description = (
            entity.description if entity.description is not None else model.description
        )

        await self.db.commit()
        await self.db.refresh(model)

        return CityEntity(
            id=model.id,
            name=model.name,
            state=model.state,
            country=model.country,
            description=model.description,
        )

    async def delete(self, city_id: int) -> bool:
        result = await self.db.execute(select(CityModel).filter(CityModel.id == city_id))
        model = result.scalar_one_or_none()
        if not model:
            return False
        await self.db.delete(model)
        await self.db.commit()
        return True

    async def search_by_name(self, name: str) -> List[CityEntity]:
        result = await self.db.execute(
            select(CityModel).filter(CityModel.name.ilike(f"%{name}%"))
        )
        cities = result.scalars().all()
        return [
            CityEntity(
                id=c.id,
                name=c.name,
                state=c.state,
                country=c.country,
                description=c.description,
            )
            for c in cities
        ]
