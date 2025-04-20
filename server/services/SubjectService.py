from server.error_handler.HTTPException import HTTPException
from server.models.Subject import Subject
from server.repositories import AlternativeRepository
from server.repositories import QuestionRepository
from server.repositories import SubjectRepository


def all() -> list[Subject]:
    return SubjectRepository.all()

def delete(id: int) -> None:
    AlternativeRepository.delete(id)
    QuestionRepository.delete(id)
    SubjectRepository.delete(id)

def find(id: int) -> Subject:
    subject = SubjectRepository.find(id)
    if not subject:
        raise HTTPException("Disciplina não encontrada", 404)
    return subject

def insert(subject: Subject) -> None:
    __validate_name(subject.name)
    if SubjectRepository.find_by_name(subject.name):
        raise HTTPException('Já existe disciplina com o nome informado.', 400)
    SubjectRepository.insert(subject)

def update(subject: Subject) -> None:
    __validate_name(subject.name)
    other_subject = SubjectRepository.find_by_name(subject.name)
    if other_subject and other_subject.id != subject.id:
        raise HTTPException('Já existe disciplina com o nome informado.', 400)
    SubjectRepository.update(subject)

def with_n_questions() -> list[Subject]:
    return SubjectRepository.with_n_questions()

def __validate_name(name: str) -> None:
    if len(name) > 63:
        raise HTTPException('Número de caracteres excedido.', 400)