from server.models.Alternative import Alternative


class Question:
    def __init__(
        self,
        statement: str,
        subject_id: int,
        id: int | None = None,
        alternatives: list[Alternative] = []
    ) -> None:
        self.id = id
        self.statement = statement
        self.subject_id = subject_id
        self.alternatives = alternatives
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "statement": self.statement,
            "subject_id": self.subject_id,
            "alternatives": [alternative.__dict__ for alternative in self.alternatives]
        }