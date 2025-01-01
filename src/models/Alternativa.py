class Alternativa:
    def __init__(self, texto: str, correto: bool, questao_id: int, id: int | None = None):
        self.texto = texto
        self.correto = correto
        self.questao_id = questao_id
        self.id = id
    
    def to_inserted_array(self):
        return [self.texto, self.correto, self.questao_id]
    
    def to_updated_array(self):
        return [self.texto, self.correto, self.questao_id, self.id]
    
    def to_dict(self):
        return {"id": self.id, "texto": self.texto, "correto": self.correto, "questao_id": self.questao_id}