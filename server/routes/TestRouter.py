from flask import Blueprint, Response, request

from server.controllers import TestController


test_blueprint = Blueprint("test", __name__, url_prefix="/tests")

@test_blueprint.route('/', methods=['GET'])
def index() -> Response:
    if request.method == 'GET': return TestController.next_question()

@test_blueprint.route('/<int:subject_id>', methods=['POST'])
def with_subject_id(subject_id: int) -> Response:
    if request.method == 'POST': return TestController.insert(subject_id)