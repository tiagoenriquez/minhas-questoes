from http import HTTPStatus


class DisciplinaException(Exception):
    def __init__(self, mensagem: str, status: HTTPStatus) -> None:
        self.mensagem = mensagem
        self.status = status
        super().__init__(mensagem)


class DisciplinaInexistenteException(DisciplinaException):
    def __init__(self) -> None:
        super().__init__(
            "Não existe disciplina com o id informado.", HTTPStatus.NOT_FOUND
        )


class DisciplinaRepetidaException(DisciplinaException):
    def __init__(self) -> None:
        super().__init__("A disciplina já foi cadastrada.", HTTPStatus.CONFLICT)


class DisciplinasInexistentesException(DisciplinaException):
    def __init__(self) -> None:
        super().__init__("Não há disciplina cadastrada.", HTTPStatus.NOT_FOUND)
