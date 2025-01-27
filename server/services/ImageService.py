from werkzeug.datastructures import FileStorage

from server.models.Image import Image
from server.models.Question import Question
from server.repositories import ImageRepository


def delete(statement: str) -> None:
    ImageRepository.delete(__get_image_name(statement))

def fetch(questions: list[Question]) -> list[Image]:
    files_names: list[str] = []
    for question in questions:
        files_names.append(__get_image_name(question.statement))
    return ImageRepository.fetch_files(files_names)

def save(question: Question, image: FileStorage) -> Question:
    question.statement = question.statement.replace(image.filename, f"@image={image.filename}")
    ImageRepository.save(image)
    return question

def __get_image_name(statement: str) -> str:
    for line in statement.splitlines():
        if line.startswith('@image='): return line[len('@image='):]