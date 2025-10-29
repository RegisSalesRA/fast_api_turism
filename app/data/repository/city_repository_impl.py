from typing import List, Optional
from sqlalchemy.orm import Session
from app.data.models.city_model import CityModel
from app.domain.entities.city_entity import CityEntity
from app.domain.repositories.city_repository import CityRepository


class CityRepositoryImpl(CityRepository):
    def __init__(self, db: Session):
        self.db = db

    def list_all(self, limit: Optional[int] = None, offset: Optional[int] = None) -> List[CityEntity]:
        query = self.db.query(CityModel)
        if offset:
            query = query.offset(offset)
        if limit:
            query = query.limit(limit)
        cities = query.all()
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

    def get_by_id(self, city_id: int) -> Optional[CityEntity]:
        c = self.db.query(CityModel).filter(CityModel.id == city_id).first()
        if not c:
            return None
        return CityEntity(
            id=c.id,
            name=c.name,
            state=c.state,
            country=c.country,
            description=c.description,
        )

    def create(self, city: CityEntity) -> CityEntity:
        model = CityModel(
            name=city.name,
            state=city.state,
            country=city.country,
            description=city.description,
        )
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return CityEntity(
            id=model.id,
            name=model.name,
            state=model.state,
            country=model.country,
            description=model.description,
        )

    def update(self, entity: CityEntity) -> Optional[CityEntity]:
        model = self.db.query(CityModel).filter(CityModel.id == entity.id).first()
        if not model:
            return None

        model.name = entity.name or model.name
        model.state = entity.state or model.state
        model.country = entity.country or model.country
        model.description = entity.description if entity.description is not None else model.description

        self.db.commit()
        self.db.refresh(model)

        return CityEntity(
            id=model.id,
            name=model.name,
            state=model.state,
            country=model.country,
            description=model.description,
        )

    def delete(self, city_id: int) -> bool:
        model = self.db.query(CityModel).filter(CityModel.id == city_id).first()
        if not model:
            return False
        self.db.delete(model)
        self.db.commit()
        return True

    def search_by_name(self, name: str) -> List[CityEntity]:
        cities = self.db.query(CityModel)\
                        .filter(CityModel.name.ilike(f"%{name}%"))\
                        .all()
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

