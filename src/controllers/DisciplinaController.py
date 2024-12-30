from flask import Blueprint, redirect, render_template, request, url_for
from src.models.Disciplina import Disciplina
from src.services import DisciplinaService


disciplina_blueprint = Blueprint("disciplina", __name__, url_prefix="/disciplina")

@disciplina_blueprint.route("/atualizacao/<int:id>", methods=["POST"])
def atualizar(id: int):
    try:
        DisciplinaService.atualizar(Disciplina(request.form.get("nome"), id))
        return redirect(url_for("disciplina.listar"))
    except Exception as exception:
        return render_template("erro.html", erro=exception.args[0])

@disciplina_blueprint.route("/cadastro")
def cadastrar():
    return render_template("cadastrarDisciplina.html")

@disciplina_blueprint.route("/edicao/<int:id>")
def editar(id: int):
    try:
        return render_template("editarDisciplina.html", disciplina=DisciplinaService.procurar(id))
    except Exception as exception:
        return render_template("erro.html", erro=exception.args[0])

@disciplina_blueprint.route("/exclusao/<int:id>", methods=["POST"])
def excluir(id: int):
    DisciplinaService.excluir(id)
    return redirect(url_for("disciplina.listar"))

@disciplina_blueprint.route("/insercao", methods=["POST"])
def inserir():
    try:
        DisciplinaService.inserir(Disciplina(request.form.get("nome")))
        return redirect(url_for("disciplina.listar"))
    except Exception as exception:
        return render_template("erro.html", erro=exception.args[0])

@disciplina_blueprint.route("/lista")
def listar():
    return render_template("listarDisciplinas.html", disciplinas=DisciplinaService.listar())

@disciplina_blueprint.route("/selecao")
def selecionar():
    return render_template("selecionarDisciplina.html", disciplinas=DisciplinaService.listar())