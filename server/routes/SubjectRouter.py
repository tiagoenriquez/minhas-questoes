from flask import Blueprint, Response, request

from server.controllers import SubjectController


subject_blueprint = Blueprint("subject", __name__, url_prefix="/subjects")

@subject_blueprint.route('/', methods=['GET', 'POST'])
def index() -> Response:
    if request.method == 'GET': return SubjectController.all()
    if request.method == 'POST': return SubjectController.insert(request)

@subject_blueprint.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def with_id(id: int) -> Response:
    if request.method == 'GET': return SubjectController.find(id)
    if request.method == 'PUT': return SubjectController.update(request, id)
    if request.method == 'DELETE': return SubjectController.delete(id)

@subject_blueprint.route('/with-n-questions', methods=['GET'])
def with_n_questions() -> Response:
    return SubjectController.with_n_questions()