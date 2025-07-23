from http import HTTPStatus
from typing import cast

from flask import jsonify, make_response, request
from marshmallow import ValidationError
from werkzeug import Response
from src.exceptions.AlternativaException import AlternativaException
from src.exceptions.QuestaoException import QuestaoException
from src.helpers.flash_errors import exibir_primeiro_erro
from src.models.Alternativa import Alternativa
from src.schemas.AlternativaSchema import AlternativaSchema
from src.services.AlternativaService import AlternativaService as service


def atualizar(id: int) -> Response:
    try:
        dados = request.get_json()
        dados["id"] = str(id)
        alternativa = cast(Alternativa, AlternativaSchema().load(dados))
        service.atualizar(alternativa)
        return make_response(
            jsonify({"mensagem": "A alternativa foi atualizad com sucesso"}),
            HTTPStatus.OK,
        )
    except ValidationError as ve:
        return make_response(jsonify({"erro": exibir_primeiro_erro(ve)}))
    except AlternativaException as ae:
        return make_response(jsonify({"erro": ae.mensagem}), ae.status)
    except Exception as e:
        return make_response(
            jsonify({"erro": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
        )


def excluir(id: int) -> Response:
    try:
        service.excluir(id)
        return make_response(
            jsonify({"mensagem": "A alternativa foi excluída com sucesso."}),
            HTTPStatus.OK,
        )
    except AlternativaException as ae:
        return make_response(jsonify({"erro": ae.mensagem}), ae.status)
    except Exception as e:
        return make_response(
            jsonify({"erro": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
        )


def inserir() -> Response:
    try:
        alternativa = cast(Alternativa, AlternativaSchema().load(request.get_json()))
        service.inserir(alternativa)
        return make_response(
            jsonify({"mensagem": "A alternativa foi salva com sucesso"}),
            HTTPStatus.CREATED,
        )
    except ValidationError as ve:
        return make_response(jsonify({"erro": exibir_primeiro_erro(ve)}))
    except AlternativaException as ae:
        return make_response(jsonify({"erro": ae.mensagem}), ae.status)
    except QuestaoException as qe:
        return make_response(jsonify({"erro": qe.mensagem}), qe.status)
    except Exception as e:
        return make_response(
            jsonify({"erro": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
        )


def procurar(id: int) -> Response:
    try:
        alternativa = service.procurar(id)
        schema = AlternativaSchema().dump(alternativa)
        return make_response(jsonify({"alternativa": schema}), HTTPStatus.OK)
    except AlternativaException as ae:
        return make_response(jsonify({"erro": ae.mensagem}), ae.status)
    except Exception as e:
        return make_response(
            jsonify({"erro": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
        )
