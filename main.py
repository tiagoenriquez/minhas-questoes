import os
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_cors import CORS

from init_db import init_db
from src.routes.AlternativaRoute import alternativa_blueprint
from src.routes.DisciplinaRouter import disciplina_blueprint
from src.routes.QuestaoRouter import questao_blueprint
from src.routes.ImagemRoute import imagem_blueprint


app = Flask(__name__, static_folder="./templates/dist/assets")


load_dotenv()


CORS(
    app,
    resources={
        r"/*": {
            "origins": ["http://localhost:5173", "http://127.0.0.1:5173"],
            "methods": ["GET", "POST", "PUT", "PATCH", "DELETE"],
        }
    },
)


app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
init_db(app)


@app.route("/")
def index() -> str:
    return render_template("dist/index.html")


@app.errorhandler(404)
def not_found(e):
    return render_template("dist/index.html")


app.register_blueprint(disciplina_blueprint)
app.register_blueprint(questao_blueprint)
app.register_blueprint(imagem_blueprint)
app.register_blueprint(alternativa_blueprint)


if __name__ == "__main__":
    app.run(port=5447, debug=True)
