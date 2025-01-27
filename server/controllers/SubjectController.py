from flask import Request, Response

from server.error_handler.HTTPException import HTTPException
from server.models.Subject import Subject
from server.response import response
from server.services import SubjectService


def all() -> Response:
    subjects = SubjectService.all()
    status_code = 200 if len(subjects) > 0 else 204
    return response([subject.__dict__ for subject in subjects], status_code)

def delete(id: int) -> Response:
    try:
        SubjectService.delete(id)
        return response('Disciplina excluída com sucesso')
    except HTTPException as exception:
        return response(exception.args[0], exception.status_code)

def find(id: int) -> Response:
    subject = SubjectService.find(id)
    status_code = 200 if subject else 204
    return response(subject.__dict__, status_code)

def insert(request: Request) -> Response:
    try:
        SubjectService.insert(Subject(request.json['name']))
        return response('Disciplina cadastrada com sucesso.', 201)
    except HTTPException as exception:
        return response(exception.args[0], exception.status_code)

def update(request: Request, id: int) -> Response:
    try:
        SubjectService.update(Subject(request.json['name'], id))
        return response('Disciplina atualizada com sucesso')
    except HTTPException as exception:
        return response(exception.args[0], exception.status_code)

def with_n_questions() -> Response:
    return response([subject.__dict__ for subject in SubjectService.with_n_questions()])