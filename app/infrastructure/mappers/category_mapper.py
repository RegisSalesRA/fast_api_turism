 

from app.data.models.category_model import CategoryModel
from app.domain.entities.category_entity import CategoryEntity


class PointTurismMapper:

    @staticmethod
    def to_entity(model: CategoryModel) -> CategoryEntity:
        return CategoryEntity(
            id=model.id,
            nome=model.name,
        )

    @staticmethod
    def to_model(entity: CategoryEntity) -> CategoryModel:
        model = CategoryModel(
            nome=entity.name, 
        )
        if entity.id:
            model.id = entity.id
        return model
