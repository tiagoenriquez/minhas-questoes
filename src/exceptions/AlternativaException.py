from http import HTTPStatus


class AlternativaException(Exception):
    def __init__(self, mensagem: str, status: HTTPStatus) -> None:
        self.mensagem = mensagem
        self.status = status
        super().__init__(mensagem)


class AlternativaInexistenteException(AlternativaException):
    def __init__(self) -> None:
        super().__init__("A alternativa não foi cadastrada.", HTTPStatus.NOT_FOUND)


class AlternativaRepetidaException(AlternativaException):
    def __init__(self) -> None:
        super().__init__(
            "Já existe outra alternativa com o mesmo texto.", HTTPStatus.CONFLICT
        )
