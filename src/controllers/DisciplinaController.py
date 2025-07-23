from http import HTTPStatus
from typing import cast
from flask import jsonify, make_response, request
from marshmallow import ValidationError
from werkzeug import Response

from src.exceptions.DisciplinaException import DisciplinaException
from src.helpers.flash_errors import exibir_primeiro_erro
from src.models.Disciplina import Disciplina
from src.schemas.DisciplinaSchema import DisciplinaSchema
from src.services.DisciplinaService import DisciplinaService as service


def atualizar(id: int) -> Response:
    try:
        dados = request.get_json()
        dados["id"] = str(id)
        disciplina = cast(Disciplina, DisciplinaSchema().load(dados))
        service.atualizar(disciplina)
        return make_response(
            jsonify({"mensagem": "A disciplina foi atualizada com sucesso"}),
            HTTPStatus.OK,
        )
    except ValidationError as ve:
        return make_response(
            jsonify({"erro": exibir_primeiro_erro(ve)}), HTTPStatus.BAD_REQUEST
        )
    except DisciplinaException as de:
        return make_response(jsonify({"erro": de.mensagem}), de.status)
    except Exception as e:
        return make_response(
            jsonify({"erro": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
        )


def excluir(id: int) -> Response:
    try:
        service.excluir(id)
        return make_response(
            jsonify({"mensagem": "A disciplina foi excluída com sucesso"}),
            HTTPStatus.OK,
        )
    except DisciplinaException as de:
        return make_response(jsonify({"erro": de.mensagem}), de.status)
    except Exception as e:
        return make_response(
            jsonify({"erro": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
        )


def inserir() -> Response:
    try:
        disciplina = cast(Disciplina, DisciplinaSchema().load(request.get_json()))
        service.inserir(disciplina)
        return make_response(
            jsonify({"mensagem": "A disciplina foi cadastrada com sucesso."}),
            HTTPStatus.CREATED,
        )
    except DisciplinaException as de:
        return make_response(jsonify({"erro": de.mensagem}), de.status)
    except Exception as e:
        return make_response(
            jsonify({"erro": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
        )


def listar() -> Response:
    try:
        disciplinas = service.listar()
        schema = DisciplinaSchema(many=True).dump(disciplinas)
        return make_response(jsonify({"disciplinas": schema}), HTTPStatus.OK)
    except DisciplinaException as de:
        return make_response(jsonify({"erro": de.mensagem}), de.status)
    except Exception as e:
        return make_response(
            jsonify({"erro": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
        )


def ordenar_por_n_questoes() -> Response:
    try:
        disciplinas = service.ordenar_por_n_questoes()
        schema = DisciplinaSchema(many=True).dump(disciplinas)
        return make_response(jsonify({"disciplinas": schema}), HTTPStatus.OK)
    except DisciplinaException as de:
        return make_response(jsonify({"erro": de.mensagem}), de.status)
    except Exception as e:
        return make_response(
            jsonify({"erro": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
        )


def procurar(id: int) -> Response:
    try:
        disciplina = service.procurar(id)
        schema = DisciplinaSchema().dump(disciplina)
        return make_response(jsonify({"disciplina": schema}), HTTPStatus.OK)
    except DisciplinaException as de:
        return make_response(jsonify({"erro": de.mensagem}), de.status)
    except Exception as e:
        return make_response(
            jsonify({"erro": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
        )
