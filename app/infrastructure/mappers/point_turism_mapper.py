from app.domain.entities.point_turism_entity import PointTurismEntity
from app.infrastructure.database.models.point_turism_model import PointTurismModel 

class PointTurismMapper:

    @staticmethod
    def to_entity(model: PointTurismModel) -> PointTurismEntity:
        return PointTurismEntity(
            id=model.id,
            nome=model.nome,
            imagem=model.imagem,
            descricao=model.descricao,
            cidade_id=model.cidade_id,
            categoria_id=model.categoria_id,
            nota_media=model.nota_media
        )

    @staticmethod
    def to_model(entity: PointTurismEntity) -> PointTurismModel:
        model = PointTurismModel(
            nome=entity.nome,
            imagem=entity.imagem,
            descricao=entity.descricao,
            cidade_id=entity.cidade_id,
            categoria_id=entity.categoria_id,
            nota_media=entity.nota_media
        )
        if entity.id:
            model.id = entity.id
        return model
