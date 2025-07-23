from http import HTTPStatus
from typing import cast
from flask import Response, jsonify, make_response, request
from marshmallow import ValidationError
from src.exceptions.DisciplinaException import DisciplinaException
from src.exceptions.QuestaoException import QuestaoException
from src.helpers.flash_errors import exibir_primeiro_erro
from src.models.Questao import Questao
from src.schemas.QuestaoSchema import QuestaoSchema
from src.services.QuestaoService import QuestaoService as service


def atualizar(id: int) -> Response:
    try:
        dados = request.get_json()
        dados["id"] = str(id)
        questao = cast(Questao, QuestaoSchema().load(dados))
        service.atualizar(questao)
        return make_response(
            jsonify({"mensagem": "A questão foi atualizada com sucesso."}),
            HTTPStatus.OK,
        )
    except ValidationError as ve:
        return make_response(
            jsonify({"erro": exibir_primeiro_erro(ve)}), HTTPStatus.BAD_REQUEST
        )
    except QuestaoException as qe:
        return make_response(jsonify({"erro": qe.mensagem}), qe.status)
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
            jsonify({"mensagem": "A questão foi excluída com sucesso."}), HTTPStatus.OK
        )
    except QuestaoException as qe:
        return make_response(jsonify({"erro": qe.mensagem}), qe.status)
    except Exception as e:
        return make_response(
            jsonify({"erro": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
        )


def inserir() -> Response:
    try:
        questao = cast(Questao, QuestaoSchema().load(request.get_json()))
        questao = service.inserir(questao)
        return make_response(
            jsonify(
                {"mensagem": "A Questão foi cadastrada com sucesso.", "id": questao.id}
            ),
            HTTPStatus.CREATED,
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


def listar(trecho: str) -> Response:
    try:
        questoes = service.listar(trecho)
        schema = QuestaoSchema(many=True).dump(questoes)
        return make_response(jsonify({"questoes": schema}), HTTPStatus.OK)
    except ValidationError as ve:
        return make_response(
            jsonify({"erro": exibir_primeiro_erro(ve)}), HTTPStatus.BAD_REQUEST
        )
    except QuestaoException as qe:
        return make_response(jsonify({"erro": qe.mensagem}), qe.status)
    except Exception as e:
        return make_response(
            jsonify({"erro": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
        )


def procurar(id: int) -> Response:
    try:
        questao = service.procurar(id)
        schema = QuestaoSchema().dump(questao)
        return make_response(jsonify({"questao": schema}), HTTPStatus.OK)
    except QuestaoException as qe:
        return make_response(jsonify({"erro": qe.mensagem}), qe.status)
    except Exception as e:
        return make_response(
            jsonify({"erro": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
        )


def sortear(disciplina_id) -> Response:
    try:
        questoes = service.sortear(disciplina_id)
        schema = QuestaoSchema(many=True).dump(questoes)
        return make_response(jsonify({"questoes": schema}), HTTPStatus.OK)
    except DisciplinaException as de:
        return make_response(jsonify({"erro": de.mensagem}), de.status)
    except Exception as e:
        return make_response(
            jsonify({"erro": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
        )
