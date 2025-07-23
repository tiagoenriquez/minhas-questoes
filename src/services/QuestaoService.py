import random
from typing import List, cast

from src.exceptions.DisciplinaException import DisciplinaInexistenteException
from src.exceptions.QuestaoException import (
    QuestaoInexistenteException,
    QuestoesInexistentesException,
)
from src.models.Alternativa import Alternativa
from src.models.Questao import Questao
from src.repositories.DisciplinaRepository import DisciplinaRepository
from src.repositories.QuestaoRepository import QuestaoRepository as repository


class QuestaoService:
    @staticmethod
    def atualizar(questao: Questao) -> None:
        repository.atualizar(questao)

    @staticmethod
    def excluir(id: int) -> None:
        questao = repository.procurar(id)
        if not questao:
            raise QuestaoInexistenteException()
        repository.excluir(questao)

    @staticmethod
    def inserir(questao: Questao) -> Questao:
        disciplina = DisciplinaRepository.procurar(questao.disciplina_id)
        if not disciplina:
            raise DisciplinaInexistenteException()
        return repository.inserir(questao)

    @staticmethod
    def listar(trecho: str) -> List[Questao]:
        questoes = repository.listar(trecho)
        if not questoes:
            raise QuestoesInexistentesException()
        return questoes

    @staticmethod
    def procurar(id: int) -> Questao:
        questao = repository.procurar(id)
        if not questao:
            raise QuestaoInexistenteException()
        return questao

    @staticmethod
    def sortear(disciplina_id: int) -> List[Questao]:
        questoes = repository.listar_por_disciplina(disciplina_id)
        random.shuffle(questoes)
        [
            random.shuffle(cast(List[Alternativa], questao.alternativas))
            for questao in questoes
        ]
        return questoes
