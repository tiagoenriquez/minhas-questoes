from server.error_handler.HTTPException import HTTPException
from server.models.Subject import Subject
from server.repositories import QuestionRepository
from server.repositories import SubjectRepository


def all() -> list[Subject]:
    return SubjectRepository.all()

def delete(id: int) -> None:
    if QuestionRepository.find_by_subject_id(id):
        raise HTTPException('Existem questões da discipliana informada', 400)
    SubjectRepository.delete(id)

def find(id: int) -> Subject:
    return SubjectRepository.find(id)

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