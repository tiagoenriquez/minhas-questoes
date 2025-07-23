from typing import List, cast
from src.exceptions.AlternativaException import (
    AlternativaInexistenteException,
    AlternativaRepetidaException,
)
from src.exceptions.QuestaoException import QuestaoInexistenteException
from src.models.Alternativa import Alternativa
from src.repositories.AlternativaRepository import AlternativaRepository as repository
from src.repositories.QuestaoRepository import QuestaoRepository


class AlternativaService:
    @staticmethod
    def atualizar(alternativa: Alternativa) -> None:
        questao = QuestaoRepository.procurar(alternativa.questao_id)
        if questao:
            for existente in cast(List[Alternativa], questao.alternativas):
                if (
                    existente.texto == alternativa.texto
                    and existente.id != alternativa.id
                ):
                    raise AlternativaRepetidaException()
        repository.atualizar(alternativa)

    @staticmethod
    def excluir(id: int) -> None:
        alternativa = repository.procurar(id)
        if not alternativa:
            raise AlternativaInexistenteException()
        repository.excluir(alternativa)

    @staticmethod
    def inserir(alternativa: Alternativa) -> None:
        questao = QuestaoRepository.procurar(alternativa.questao_id)
        if not questao:
            raise QuestaoInexistenteException()
        for existente in cast(List[Alternativa], questao.alternativas):
            if existente.texto == alternativa.texto:
                raise AlternativaRepetidaException()
        repository.inserir(alternativa)

    @staticmethod
    def procurar(id: int) -> Alternativa:
        alternativa = repository.procurar(id)
        if not alternativa:
            raise AlternativaInexistenteException()
        return alternativa
