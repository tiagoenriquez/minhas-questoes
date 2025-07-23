from marshmallow import Schema, fields, post_load, validate
from typing import TYPE_CHECKING
from src.models.Disciplina import Disciplina


class DisciplinaSchema(Schema):
    id = fields.Int()

    nome = fields.Str(
        required=True,
        validate=validate.Length(
            min=1, max=63, error="O nome deve ter no máximo 63 caracteres."
        ),
        error_messages={
            "required": "O nome é obrigatório.",
            "invalid": "Formato inválido para nome.",
        },
    )

    n_questoes = fields.Method("get_n_questoes")

    @post_load
    def make_disciplina(self, data, **kwargs) -> Disciplina:
        return Disciplina(**data)

    def get_n_questoes(self, obj) -> int:
        return obj.n_questoes
