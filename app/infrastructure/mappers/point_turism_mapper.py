from app.data.models.point_turism_model import PointTurismModel
from app.domain.entities.point_turism_entity import PointTurismEntity 

class PointTurismMapper:

    @staticmethod
    def to_entity(model: PointTurismModel) -> PointTurismEntity:
        return PointTurismEntity(
            id=model.id,
            name=model.name,
            image=model.image,
            description=model.description,
            review=model.review
        )

    @staticmethod
    def to_model(entity: PointTurismEntity) -> PointTurismModel:
        model = PointTurismModel(
            name=entity.name,
            image=entity.image,
            description=entity.description,
            review=entity.review
        )
        if entity.id:
            model.id = entity.id
        return model
