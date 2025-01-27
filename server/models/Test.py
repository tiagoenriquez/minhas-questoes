from server.models.Image import Image
from server.models.Question import Question


class Test:
    def __init__(self, questions: list[Question], grade: float, images: list[Image]):
        self.questions = questions
        self.grade = grade
        self.images = images

    def to_dict(self) -> dict:
        return {
            "questions": [question.to_dict() for question in self.questions],
            "grade": self.grade,
            "images": [image.__dict__ for image in self.images]
        }