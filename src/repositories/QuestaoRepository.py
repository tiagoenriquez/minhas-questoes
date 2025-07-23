from typing import List
from src.connections.DatabaseConnection import db
from src.exceptions.QuestaoException import QuestaoInexistenteException
from src.exceptions.DisciplinaException import DisciplinaInexistenteException
from src.models.Disciplina import Disciplina
from src.models.Questao import Questao


class QuestaoRepository:
    @staticmethod
    def atualizar(questao: Questao) -> None:
        existente = Questao.query.get(questao.id)
        if not existente:
            raise QuestaoInexistenteException()
        existente.enunciado = questao.enunciado
        existente.disciplina_id = questao.disciplina_id
        db.session.commit()

    @staticmethod
    def excluir(questao: Questao) -> None:
        db.session.delete(questao)
        db.session.commit()

    @staticmethod
    def inserir(questao: Questao) -> Questao:
        db.session.add(questao)
        db.session.commit()
        return questao

    @staticmethod
    def listar(trecho: str) -> List[Questao]:
        return Questao.query.filter(Questao.enunciado.ilike(f"%{trecho}%")).all()

    @staticmethod
    def listar_por_disciplina(disciplina_id: int) -> List[Questao]:
        disciplina: Disciplina | None = Disciplina.query.get(disciplina_id)
        if not disciplina:
            raise DisciplinaInexistenteException()
        return disciplina.questoes_validas

    @staticmethod
    def procurar(id: int) -> Questao | None:
        return Questao.query.get(id)
