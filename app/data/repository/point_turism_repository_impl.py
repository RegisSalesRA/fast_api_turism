from typing import List, Optional
from sqlalchemy.orm import Session
from app.data.models.point_turism_model import PointTurismModel
from app.domain.entities.point_turism_entity import PointTurismEntity
from app.domain.repositories.point_turism_repository import PointTurismRepository


class PointTurismRepositoryImpl(PointTurismRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[PointTurismEntity]:
        points = self.db.query(PointTurismModel).all()
        return [
            PointTurismEntity(
                id=p.id,
                name=p.name,
                image=p.image,
                description=p.description,
                city_id=p.city_id,
                category_id=p.category_id,
                review=p.review,
            )
            for p in points
        ]

    def get_by_id(self, point_id: int) -> Optional[PointTurismEntity]:
        p = self.db.query(PointTurismModel).filter(PointTurismModel.id == point_id).first()
        if not p:
            return None
        return PointTurismEntity(
            id=p.id,
            name=p.name,
            image=p.image,
            description=p.description,
            city_id=p.city_id,
            category_id=p.category_id,
            review=p.review,
        )

    def create(self, point: PointTurismEntity) -> PointTurismEntity:
        model = PointTurismModel(
            name=point.name,
            image=point.image,
            description=point.description,
            city_id=point.city_id,
            category_id=point.category_id,
            review=point.review,
        )
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return PointTurismEntity(
            id=model.id,
            name=model.name,
            image=model.image,
            description=model.description,
            city_id=model.city_id,
            category_id=model.category_id,
            review=model.review,
        )

    def update(self, point_id: int, data: dict) -> Optional[PointTurismEntity]:
        model = self.db.query(PointTurismModel).filter(PointTurismModel.id == point_id).first()
        if not model:
            return None

        for key, value in data.items():
            setattr(model, key, value)
        self.db.commit()
        self.db.refresh(model)

        return PointTurismEntity(
            id=model.id,
            name=model.name,
            image=model.image,
            description=model.description,
            city_id=model.city_id,
            category_id=model.category_id,
            review=model.review,
        )

    def delete(self, point_id: int) -> bool:
        model = self.db.query(PointTurismModel).filter(PointTurismModel.id == point_id).first()
        if not model:
            return False
        self.db.delete(model)
        self.db.commit()
        return True
