class Alternative:
    def __init__(
        self, alternative_text: str,
        correct: bool,
        question_id: int | None = None,
        id: int | None = None
    ) -> None:
        self.id = id
        self.alternative_text = alternative_text
        self.correct = correct
        self.question_id = question_id