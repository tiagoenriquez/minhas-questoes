from marshmallow import Schema, fields, post_load
from src.schemas.AlternativaSchema import AlternativaSchema
from src.schemas.DisciplinaSchema import DisciplinaSchema
from src.models.Questao import Questao


class QuestaoSchema(Schema):
    id = fields.Int()

    enunciado = fields.Str(
        required=True, error_messages={"required": "O enunciado é obrigatório."}
    )

    disciplina_id = fields.Int(
        required=True, error_messages={"required": "Você deve escolher uma disciplina."}
    )

    disciplina = fields.Nested(DisciplinaSchema)

    valida = fields.Method("get_valida")

    alternativas = fields.Nested(AlternativaSchema, many=True)

    @post_load
    def make_questao(self, data, **kwargs) -> Questao:
        return Questao(**data)

    def get_valida(self, obj) -> bool:
        return obj.valida
