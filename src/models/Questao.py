from src.models.Disciplina import Disciplina
from src.models.Alternativa import Alternativa


class Questao:
    def __init__(
        self, enunciado: str,
        disciplina_id: int,
        id: int | None = None,
        disciplina: Disciplina | None = None,
        alternativas: list[Alternativa] = []
    ):
        self.enunciado = enunciado
        self.disciplina_id = disciplina_id
        self.id = id
        self.disciplina = disciplina
        self.alternativas = alternativas
    
    def to_inserted_array(self):
        return [self.enunciado, self.disciplina_id]
    
    def to_updated_array(self):
        return [self.enunciado, self.disciplina_id, self.id]
    
    def to_dict(self):
        return {
            "id": self.id,
            "enunciado": self.enunciado,
            "disciplina_id": self.disciplina_id,
            "disciplina": self.disciplina.to_dict(),
            "alternativas": [alternativa.to_dict() for alternativa in self.alternativas]
        }