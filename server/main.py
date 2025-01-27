from flask import Flask, render_template
from flask_cors import CORS

from server.routes.QuestionRouter import question_blueprint
from server.routes.SubjectRouter import subject_blueprint
from server.routes.TestRouter import test_blueprint


app = Flask(__name__, template_folder='../templates', static_folder='../static')

CORS(app, resources={r"/*": {
    "origins": ["http://localhost:5173", "http://localhost:11208", "http://127.0.0.1:11208"],
    "methods": ["GET", "POST", "PUT", "PATCH", "DELETE"],
}})

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

app.register_blueprint(subject_blueprint)
app.register_blueprint(question_blueprint)
app.register_blueprint(test_blueprint)