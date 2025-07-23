from flask import Blueprint
from src.controllers.QuestaoController import (
    atualizar,
    excluir,
    inserir,
    listar,
    procurar,
    sortear,
)


questao_blueprint = Blueprint("questao", __name__, url_prefix="/questoes")

questao_blueprint.add_url_rule("/<int:id>", view_func=procurar, methods=["GET"])
questao_blueprint.add_url_rule(
    "/lista/<string:trecho>", view_func=listar, methods=["GET"]
)
questao_blueprint.add_url_rule(
    "/sorteio/<int:disciplina_id>", view_func=sortear, methods=["GET"]
)
questao_blueprint.add_url_rule("/", view_func=inserir, methods=["POST"])
questao_blueprint.add_url_rule("/<int:id>", view_func=atualizar, methods=["PUT"])
questao_blueprint.add_url_rule("/<int:id>", view_func=excluir, methods=["DELETE"])
