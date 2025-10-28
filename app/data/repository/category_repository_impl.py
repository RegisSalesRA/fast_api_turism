from typing import List, Optional
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.data.models.category_model import CategoryModel
from app.domain.entities.category_entity import CategoryEntity
from app.domain.repositories.category_repository import CategoryRepository 


class CategoryRepositoryImpl(CategoryRepository):
    def __init__(self, db: Session):
        self.db = db

    def list_all(self, limit: Optional[int] = None, offset: Optional[int] = None) -> List[CategoryModel]:
        query = self.db.query(CategoryModel)
        if offset:
            query = query.offset(offset)
        if limit:
            query = query.limit(limit)
        points = query.all()
        return [
            CategoryModel(
                id=p.id,
                name=p.name, 
            )
            for p in points
        ]

    def get_by_id(self, point_id: int) -> Optional[CategoryModel]:
        p = self.db.query(CategoryModel).filter(CategoryModel.id == point_id).first()
        if not p:
            return None
        return CategoryModel(
            id=p.id,
            name=p.name, 
        )

    def create(self, point: CategoryModel) -> CategoryModel:
        model = CategoryModel(
            name=point.name, 
        )
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return CategoryModel(
            id=model.id,
            name=model.name, 
        )

    def update(self, entity: CategoryEntity) -> Optional[CategoryEntity]:
        model = self.db.query(CategoryModel).filter(CategoryModel.id == entity.id).first()
        if not model:
            return None

        model.name = entity.name or model.name
        self.db.commit()
        self.db.refresh(model)

        return CategoryEntity(
        id=model.id,
        name=model.name,
    )


    def delete(self, point_id: int) -> bool:
        model = self.db.query(CategoryModel).filter(CategoryModel.id == point_id).first()
        if not model:
            return False
        self.db.delete(model)
        self.db.commit()
        return True

    def search_by_name(self, name: str) -> List[CategoryModel]:
        points = self.db.query(CategoryModel)\
                        .filter(CategoryModel.name.ilike(f"%{name}%"))\
                        .all()
        return [
            CategoryModel(
                id=p.id,
                name=p.name, 
            )
            for p in points
        ]
 