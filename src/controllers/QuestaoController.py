from flask import Blueprint, redirect, render_template, request, url_for
from src.services import DisciplinaService


questao_blueprint = Blueprint("questao", __name__, url_prefix="/questao")

@questao_blueprint.route("/cadastro")
def cadastrar():
    return render_template("cadastrarQuestao.html", disciplinas=DisciplinaService.listar())

@questao_blueprint.route("/busca")
def procurar():
    return render_template("procurarQuestoes.html")