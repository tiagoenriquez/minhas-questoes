class Disciplina:
    def __init__(self, nome: str, id: int | None = None):
        self.nome = nome
        self.id = id
    
    def to_inserted_array(self):
        return [self.nome]
    
    def to_updated_array(self):
        return [self.nome, self.id]
    
    def to_dict(self):
        return { "id": self.id, "nome": self.nome }