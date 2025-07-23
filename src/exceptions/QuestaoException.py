from http import HTTPStatus


class QuestaoException(Exception):
    def __init__(self, mensagem: str, status: HTTPStatus) -> None:
        self.mensagem = mensagem
        self.status = status
        super().__init__(mensagem)


class QuestaoInexistenteException(QuestaoException):
    def __init__(self) -> None:
        super().__init__("A questão não foi cadastrada.", HTTPStatus.NOT_FOUND)


class QuestoesInexistentesException(QuestaoException):
    def __init__(self) -> None:
        super().__init__(
            "Não há questão cadastrada com o trecho informado.", HTTPStatus.NOT_FOUND
        )
