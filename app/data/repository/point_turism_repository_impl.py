from typing import List, Optional
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.data.models.point_turism_model import PointTurismModel
from app.domain.entities.point_turism_entity import PointTurismEntity
from app.domain.repositories.point_turism_repository import PointTurismRepository


class PointTurismRepositoryImpl(PointTurismRepository):
    def __init__(self, db: Session):
        self.db = db

    def list_all(self, limit: Optional[int] = None, offset: Optional[int] = None) -> List[PointTurismEntity]:
        query = self.db.query(PointTurismModel)
        if offset:
            query = query.offset(offset)
        if limit:
            query = query.limit(limit)
        points = query.all()
        return [
            PointTurismEntity(
                id=p.id,
                name=p.name,
                image=p.image,
                description=p.description, 
                category_id=1,
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
            category_id=p.category_id,
            review=p.review,
        )

    def create(self, point: PointTurismEntity) -> PointTurismEntity:
        model = PointTurismModel(
            name=point.name,
            image=point.image,
            description=point.description,
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
            category_id=1,
            review=model.review,
        )

    def update(self, entity: PointTurismEntity) -> Optional[PointTurismEntity]:
        
        model = (
        self.db.query(PointTurismModel)
        .filter(PointTurismModel.id == entity.id)
        .first()
    ) 
        if not model:
            return None 
        model.name = entity.name or model.name
        model.image = entity.image or model.image
        model.description = entity.description if entity.description is not None else model.description
        model.category_id = entity.category_id or model.category_id
        model.review = entity.review if entity.review is not None else model.review

        self.db.commit()
        self.db.refresh(model)

        return PointTurismEntity(
        id=model.id,
        name=model.name,
        image=model.image,
        description=model.description,
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

    def search_by_name(self, name: str) -> List[PointTurismEntity]:
        points = self.db.query(PointTurismModel)\
                        .filter(PointTurismModel.name.ilike(f"%{name}%"))\
                        .all()
        return [
            PointTurismEntity(
                id=p.id,
                name=p.name,
                image=p.image,
                description=p.description, 
                category_id=p.category_id,
                review=p.review,
            )
            for p in points
        ]
 
    def filter(
        self, 
        category_id: Optional[int] = None,
        min_review: Optional[float] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> List[PointTurismEntity]:
        query = self.db.query(PointTurismModel)
 
        if category_id is not None:
            query = query.filter(PointTurismModel.category_id == category_id)
        if min_review is not None:
            query = query.filter(PointTurismModel.review >= min_review)
        if offset is not None:
            query = query.offset(offset)
        if limit is not None:
            query = query.limit(limit)

        points = query.all()
        return [
            PointTurismEntity(
                id=p.id,
                name=p.name,
                image=p.image,
                description=p.description, 
                category_id=p.category_id,
                review=p.review,
            )
            for p in points
        ]
 