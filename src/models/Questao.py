from typing import cast
from src.connections.DatabaseConnection import db


class Questao(db.Model):
    __tablename__ = "questoes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    enunciado = db.Column(db.Text, nullable=False)
    disciplina_id = db.Column(
        db.Integer, db.ForeignKey("disciplinas.id"), nullable=False
    )

    disciplina = db.relationship("Disciplina", back_populates="questoes")
    alternativas = db.relationship(
        "Alternativa", back_populates="questao", cascade="all, delete-orphan"
    )

    @property
    def valida(self) -> bool:
        alternativas = cast(list, self.alternativas)
        corretas = [alternativa for alternativa in alternativas if alternativa.correta]
        erradas = [
            alternativa for alternativa in alternativas if not alternativa.correta
        ]
        return len(corretas) == 1 and len(erradas) >= 1
