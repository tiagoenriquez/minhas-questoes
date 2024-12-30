from src.connections.DatabaseConnection import con
from src.models.Disciplina import Disciplina


def atualizar(disciplina: Disciplina):
    with con:
        con.execute("update disciplinas set nome = ? where id = ?", disciplina.to_updated_array())
        con.commit()

def excluir(id: int):
    with con:
        con.execute("delete from disciplinas where id = ?", [id])
        con.commit()

def inserir(disciplina: Disciplina):
    with con:
        con.execute("insert into disciplinas (nome) values (?)", disciplina.to_inserted_array())
        con.commit()

def listar():
    with con:
        cur = con.cursor()
        cur.execute("select * from disciplinas order by nome")
        disciplinas: list[Disciplina] = []
        for row in cur.fetchall():
            disciplinas.append(Disciplina(row[1], row[0]))
        return disciplinas

def procurar(id: int):
    with con:
        cur = con.cursor()
        cur.execute("select * from disciplinas where id = ?", [id])
        res = cur.fetchone()
        if not res:
            return None
        return Disciplina(res[1], res[0])

def procurarPorNome(nome: str):
    with con:
        cur = con.cursor()
        cur.execute("select * from disciplinas where nome = ?", [nome])
        res = cur.fetchone()
        if not res:
            return None
        return Disciplina(res[1], res[0])