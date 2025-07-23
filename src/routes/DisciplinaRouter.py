from flask import Blueprint
from src.controllers.DisciplinaController import (
    atualizar,
    excluir,
    inserir,
    listar,
    ordenar_por_n_questoes,
    procurar,
)


disciplina_blueprint = Blueprint("disciplina", __name__, url_prefix="/disciplinas")

disciplina_blueprint.add_url_rule("/", view_func=listar, methods=["GET"])
disciplina_blueprint.add_url_rule(
    "/ordenadas-por-n-questoes", view_func=ordenar_por_n_questoes, methods=["GET"]
)
disciplina_blueprint.add_url_rule("/<int:id>", view_func=procurar, methods=["GET"])
disciplina_blueprint.add_url_rule("/", view_func=inserir, methods=["POST"])
disciplina_blueprint.add_url_rule("/<int:id>", view_func=atualizar, methods=["PUT"])
disciplina_blueprint.add_url_rule("/<int:id>", view_func=excluir, methods=["DELETE"])
