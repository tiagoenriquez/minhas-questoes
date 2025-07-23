from marshmallow import Schema, fields, post_load
from src.models.Alternativa import Alternativa


class AlternativaSchema(Schema):
    id = fields.Int()

    texto = fields.Str(
        required=True,
        error_messages={"required": "O texto da alternativa é obrigatório."},
    )

    correta = fields.Bool(
        required=True,
        truthy=["1", "true", "True", True],
        falsy=["0", "false", "False", False],
        error_messages={
            "required": "Você precisa informar se a alternativa é correta.",
            "invalid": "Um valor inválido foi informado para o campo correta.",
        },
    )

    justificativa = fields.Str(required=False)

    questao_id = fields.Int(
        required=True, error_messages={"required": "O id da questão não foi informado."}
    )

    @post_load
    def make_alternativa(self, data, **kwargs) -> Alternativa:
        return Alternativa(**data)
