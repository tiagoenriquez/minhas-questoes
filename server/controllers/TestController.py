from flask import Request, Response

from server.error_handler.HTTPException import HTTPException
from server.response import response
from server.services import TestService


def insert(subject_id: int) -> Response:
    try:
        return response(TestService.create(subject_id).to_dict(), 201)
    except HTTPException as exception:
        return response(exception.args[0], exception.status_code)