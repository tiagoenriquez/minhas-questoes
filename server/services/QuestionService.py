from werkzeug.datastructures import FileStorage

from server.error_handler.HTTPException import HTTPException
from server.models.Alternative import Alternative
from server.models.Question import Question
from server.repositories import AlternativeRepository
from server.repositories import SubjectRepository
from server.repositories import QuestionRepository
from server.services import ImageService


def delete(id: int) -> None:
    question = QuestionRepository.find_by_id(id)
    if '@image=' in question.statement:
        ImageService.delete(question.statement)
    AlternativeRepository.delete(id)
    QuestionRepository.delete(id)

def find_by_excerpt(excerpt: str) -> list[Question]:
    return QuestionRepository.find_by_excerpt(f"%{excerpt}%")

def find_by_id(id: int) -> Question:
    return QuestionRepository.find_by_id(id)

def insert(question: Question, image: FileStorage | None = None) -> None:
    __check_subject(question.subject_id)
    if image: question = ImageService.save(question, image)
    __check_alternatives(question.alternatives)
    AlternativeRepository.insert(question.alternatives, QuestionRepository.insert(question))

def update(question: Question) -> None:
    __check_subject(question.subject_id)
    __check_alternatives(question.alternatives)
    QuestionRepository.update(question)
    AlternativeRepository.update(question.alternatives)

def __check_alternatives(alternatives: list[Alternative]) -> None:
    corrects = 0
    for i, alternative in enumerate(alternatives):
        if alternative.correct: corrects += 1
        if corrects > 1: raise HTTPException('Mais de uma alternativa correta', 400)
        for other_alternative in alternatives[i + 1:]:
            if alternative.alternative_text == other_alternative.alternative_text:
                raise HTTPException('Mais de uma alternativa com o mesmo texto', 400)
    if corrects == 0: raise HTTPException('Questão sem alternativa correta', 400)

def __check_subject(subject_id: int) -> None:
    if not SubjectRepository.count(): raise HTTPException('Disciplina não cadastrada', 400)