from flask import Blueprint, Response, request

from server.controllers import QuestionController


question_blueprint = Blueprint("question", __name__, url_prefix="/questions")

@question_blueprint.route('/', methods=['GET', 'POST'])
def index() -> Response:
    if request.method == 'POST':
        return QuestionController.insert(request)
    if request.method == 'GET':
        return QuestionController.find_by_excerpt(request)

@question_blueprint.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def with_id(id: int) -> Response:
    if request.method == 'GET':
        return QuestionController.find_by_id(id)
    if request.method == 'PUT':
        return QuestionController.update(request, id)
    if request.method == 'DELETE':
        return QuestionController.delete(id)