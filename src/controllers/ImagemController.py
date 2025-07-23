import os
from flask import Response, jsonify, make_response, request, send_from_directory
from http import HTTPStatus

from src.services.ImagemService import ImagemService as service


def salvar() -> Response:
    if "imagens" in request.files:
        imagens = request.files.getlist("imagens")
        service.salvar(imagens)
        return make_response(
            jsonify({"mensagem": "As imagens foram salvas com sucesso."}), HTTPStatus.OK
        )
    return make_response(
        jsonify({"erro": "As imagens não foram enviadas para persistência."}),
        HTTPStatus.BAD_REQUEST,
    )


def recuperar(nome: str) -> Response:
    diretorio = os.path.abspath(service.get_uploaded_folder())
    return send_from_directory(diretorio, nome)
