from flask import Blueprint
from src.controllers.ImagemController import recuperar, salvar


imagem_blueprint = Blueprint("imagem", __name__, url_prefix="/upload")

imagem_blueprint.add_url_rule("/<string:nome>", view_func=recuperar, methods=["GET"])
imagem_blueprint.add_url_rule("/", view_func=salvar, methods=["POST"])
