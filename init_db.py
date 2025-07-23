from flask import Flask

from src.connections.DatabaseConnection import db
from src.models import Disciplina, Questao, Alternativa


def init_db(app: Flask) -> None:
    db.init_app(app)
    with app.app_context():
        db.create_all()
        print("🔧 Banco de dados inicializado com sucesso.")
