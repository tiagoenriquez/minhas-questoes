from src.connections.DatabaseConnection import con
from src.models.Questao import Questao


def inserir(questao: Questao):
    with con:
        con.execute("insert into questoes (enunciado, disciplina_id), values(?, ?)", questao.to_inserted_array())
        con.commit()