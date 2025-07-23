from typing import List
from src.connections.DatabaseConnection import db
from src.exceptions.AlternativaException import AlternativaInexistenteException
from src.models.Alternativa import Alternativa


class AlternativaRepository:
    @staticmethod
    def atualizar(alternativa: Alternativa) -> None:
        existente = Alternativa.query.get(alternativa.id)
        if not existente:
            raise AlternativaInexistenteException()
        existente.texto = alternativa.texto
        existente.correta = alternativa.correta
        existente.justificativa = alternativa.justificativa
        db.session.commit()

    @staticmethod
    def excluir(alternativa: Alternativa) -> None:
        db.session.delete(alternativa)
        db.session.commit()

    @staticmethod
    def inserir(alternativa: Alternativa) -> None:
        db.session.add(alternativa)
        db.session.commit()

    @staticmethod
    def listar_por_texto(texto: str) -> List[Alternativa]:
        return Alternativa.query.filter_by(texto=texto).all()

    @staticmethod
    def procurar(id: int) -> Alternativa | None:
        return Alternativa.query.get(id)
