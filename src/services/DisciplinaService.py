from typing import List
from src.exceptions.DisciplinaException import (
    DisciplinaInexistenteException,
    DisciplinaRepetidaException,
)
from src.models.Disciplina import Disciplina
from src.models.Questao import Questao
from src.repositories.DisciplinaRepository import DisciplinaRepository as repository


class DisciplinaService:
    @staticmethod
    def atualizar(disciplina: Disciplina) -> None:
        outra = repository.procurar_por_nome(disciplina.nome)
        if outra and outra.id != disciplina.id:
            raise DisciplinaRepetidaException()
        repository.atualizar(disciplina)

    @staticmethod
    def excluir(id: int) -> None:
        disciplina = repository.procurar(id)
        if not disciplina:
            raise DisciplinaInexistenteException()
        repository.excluir(disciplina)

    @staticmethod
    def inserir(disciplina: Disciplina) -> None:
        existente = repository.procurar_por_nome(disciplina.nome)
        if existente:
            raise DisciplinaRepetidaException()
        repository.inserir(disciplina)

    @staticmethod
    def listar() -> List[Disciplina]:
        return repository.listar()

    @staticmethod
    def ordenar_por_n_questoes() -> List[Questao]:
        return repository.ordenar_por_n_questoes()

    @staticmethod
    def procurar(id: int) -> Disciplina:
        disciplina = repository.procurar(id)
        if not disciplina:
            raise DisciplinaInexistenteException()
        return disciplina
