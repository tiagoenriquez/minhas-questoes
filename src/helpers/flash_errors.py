from flask import flash
from marshmallow import ValidationError
from typing import cast


def exibir_primeiro_erro(e: ValidationError) -> str:
    mensagens = cast(dict[str, list[str]], e.messages)
    if mensagens:
        primeira = next(iter(mensagens.values()))[0]
        return primeira
    return "Erro de validação desconhecida"
