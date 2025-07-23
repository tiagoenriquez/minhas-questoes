from flask import Blueprint
from src.controllers.AlternativaController import atualizar, excluir, inserir, procurar


alternativa_blueprint = Blueprint("alternativa", __name__, url_prefix="/alternativas")

alternativa_blueprint.add_url_rule("/<int:id>", view_func=procurar, methods=["GET"])
alternativa_blueprint.add_url_rule("/", view_func=inserir, methods=["POST"])
alternativa_blueprint.add_url_rule("/<int:id>", view_func=atualizar, methods=["PATCH"])
alternativa_blueprint.add_url_rule("/<int:id>", view_func=excluir, methods=["DELETE"])
