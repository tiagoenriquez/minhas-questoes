from flask import Flask, redirect
from src.controllers.DisciplinaController import disciplina_blueprint
from src.controllers.QuestaoController import questao_blueprint
from src.migrations.migrate import migrate


migrate()
app = Flask(__name__)
app.register_blueprint(disciplina_blueprint)
app.register_blueprint(questao_blueprint)

@app.route("/")
def init():
    return redirect("/disciplina/selecao")