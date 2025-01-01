from src.connections.DatabaseConnection import con
from src.models.Alternativa import Alternativa


def inserir(alternativa: Alternativa):
    with con:
        con.execute(
            "insert into alternativa (texto, correto, questao_id) values (?, ?, ?)",
            alternativa.to_inserted_array()
        )
        con.commit()