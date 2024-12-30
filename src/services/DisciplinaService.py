from src.models import Disciplina
from src.repositories import DisciplinaRepository


def atualizar(disciplina: Disciplina):
    outra_disciplina = DisciplinaRepository.procurarPorNome(disciplina.nome)
    if outra_disciplina and outra_disciplina.id != disciplina.id:
        raise Exception("Já existe outra disciplina cadastrada com o mesmo nome.")
    DisciplinaRepository.atualizar(disciplina)

def excluir(id: int):
    DisciplinaRepository.excluir(id)

def inserir(disciplina: Disciplina):
    if DisciplinaRepository.procurarPorNome(disciplina.nome):
        raise Exception("Disciplina já cadastrada.")
    DisciplinaRepository.inserir(disciplina)

def listar():
    return DisciplinaRepository.listar()

def procurar(id: int):
    disciplina = DisciplinaRepository.procurar(id)
    if not disciplina:
        raise Exception("Não existe disciplina com o id informado.")
    return disciplina