import json

from flask import Request, Response
from werkzeug.datastructures import FileStorage

from server.error_handler.HTTPException import HTTPException
from server.models.Alternative import Alternative
from server.models.Question import Question
from server.response import response
from server.services import QuestionService


def delete(id: int) -> Response:
    QuestionService.delete(id)
    return response('Questão excluída com sucesso')

def find_by_excerpt(request: Request) -> Response:
    questions: list[dict] = []
    for question in QuestionService.find_by_excerpt(request.args.get('trecho')):
        questions.append(question.__dict__)
    return response(questions)

def find_by_id(id: int) -> Response:
    return response(QuestionService.find_by_id(id).to_dict())

def insert(request: Request) -> Response:
    try:
        alternatives: list[Alternative] = []
        for alternative in json.loads(request.form['alternatives']):
            alternatives.append(Alternative(alternative['text'], alternative['correct']))
        image: FileStorage | None = request.files.get('image') if request.files else None
        QuestionService.insert(
            Question(request.form['statement'], request.form['subject_id'], alternatives=alternatives),
            image
        )
        return response('Questão cadastrada com sucess', 201)
    except HTTPException as exception:
        return response(exception.args[0], exception.status_code)

def update(request: Request, id: int) -> Response:
    try:
        alternatives: list[Alternative] = []
        for alternative in request.json['alternatives']:
            alternatives.append(Alternative(
                alternative['text'],
                alternative['correct'],
                question_id=id,
                id=alternative['id']
            ))
        QuestionService.update(Question(request.json['statement'], request.json['subject_id'], id, alternatives))
        return response('Questão atualizada com sucesso', 200)
    except HTTPException as exception:
        return response(exception.args[0], exception.status_code)