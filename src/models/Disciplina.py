from typing import List, cast
from src.connections.DatabaseConnection import db


class Disciplina(db.Model):
    __tablename__ = "disciplinas"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(63), nullable=False, unique=True)

    questoes = db.relationship(
        "Questao", back_populates="disciplina", cascade="all, delete-orphan"
    )

    @property
    def questoes_validas(self) -> List:
        return [questao for questao in cast(List, self.questoes) if questao.valida]

    @property
    def n_questoes(self) -> int:
        return len(self.questoes_validas)
