from typing import List

from sqlalchemy import func
from src.exceptions.DisciplinaException import DisciplinaInexistenteException
from src.connections.DatabaseConnection import db
from src.models.Disciplina import Disciplina
from src.models.Questao import Questao


class DisciplinaRepository:
    @staticmethod
    def atualizar(disciplina: Disciplina) -> None:
        existente = Disciplina.query.get(disciplina.id)
        if not existente:
            raise DisciplinaInexistenteException()
        existente.nome = disciplina.nome
        db.session.commit()

    @staticmethod
    def excluir(disciplina: Disciplina) -> None:
        db.session.delete(disciplina)
        db.session.commit()

    @staticmethod
    def inserir(disciplina: Disciplina) -> None:
        db.session.add(disciplina)
        db.session.commit()

    @staticmethod
    def listar() -> List[Disciplina]:
        return Disciplina.query.order_by("nome").all()

    @staticmethod
    def ordenar_por_n_questoes() -> List[Questao]:
        query = (
            db.session.query(Disciplina, func.count(Questao.id).label("n_questao"))
            .outerjoin(Questao, Disciplina.id == Questao.disciplina_id)
            .group_by(Disciplina.id)
            .order_by(func.count(Questao.id).desc())
            .order_by(Disciplina.nome.asc())
        )
        return [row[0] for row in query]

    @staticmethod
    def procurar(id: int) -> Disciplina | None:
        return Disciplina.query.get(id)

    @staticmethod
    def procurar_por_nome(nome: str) -> Disciplina | None:
        return Disciplina.query.filter_by(nome=nome).first()
