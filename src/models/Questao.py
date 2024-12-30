from src.models.Disciplina import Disciplina


class Questao:
    def __init__(
        self, enunciado: str,
        disciplina_id: int,
        disciplina: Disciplina | None = None,
        id: int | None = None
    ):
        self.enunciado = enunciado
        self.disciplina_id = disciplina_id
        self.disciplina = disciplina
        self.id = id
    
    def to_inserted_array(self):
        return [self.enunciado, self.disciplina_id]
    
    def to_updated_array(self):
        return [self.enunciado, self.disciplina_id, self.id]
    
    def to_dict(self):
        return {
            "id": self.id,
            "enunciado": self.enunciado,
            "disciplina_id": self.disciplina_id,
            "disciplina": self.disciplina
        }