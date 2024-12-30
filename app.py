from flask import Flask
from src.controllers.DisciplinaController import disciplina_blueprint
from src.migrations.migrate import migrate


migrate()
app = Flask(__name__)
app.register_blueprint(disciplina_blueprint)