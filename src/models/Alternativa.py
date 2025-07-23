from src.connections.DatabaseConnection import db


class Alternativa(db.Model):
    __tablename__ = "alternativas"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    texto = db.Column(db.Text, nullable=False)
    correta = db.Column(db.Boolean, nullable=False)
    justificativa = db.Column(db.Text, nullable=False)
    questao_id = db.Column(db.Integer, db.ForeignKey("questoes.id"), nullable=False)

    questao = db.relationship("Questao", back_populates="alternativas")
