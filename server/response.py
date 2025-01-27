import json

from flask import Response


def response(content: any, status: int = 200, type: str = 'application/json') -> Response:
    return Response(json.dumps(content), status, mimetype=type)