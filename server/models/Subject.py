class Subject:
    def __init__(self, name: str, id: int | None = None, n_questions: int | None = None) -> None:
        self.id = id
        self.name = name
        self.n_questions = n_questions