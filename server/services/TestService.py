from server.error_handler.HTTPException import HTTPException
from server.models.Question import Question
from server.models.Test import Test
from server.repositories import QuestionRepository
from server.services import ImageService
from server.utils.drawner import draw


def create(subject_id: int) -> Test:
    questions: list[Question] = draw(QuestionRepository.find_by_subject_id(subject_id), True)
    if not questions:
        raise HTTPException('Disciplina sem questões cadastradas', 400)
    for question in questions:
        question.alternatives = draw(question.alternatives)
    return Test(questions, 0, ImageService.fetch(questions))