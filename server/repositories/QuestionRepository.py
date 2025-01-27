from server.connections.DatabaseConnection import connection
from server.models.Alternative import Alternative
from server.models.Question import Question


def delete(id: int) -> None:
    with connection:
        connection.execute('delete from questions where id = ?', [id])
        connection.commit()

def find_by_excerpt(excerpt: str) -> list[Question]:
    with connection:
        cursor = connection.cursor()
        cursor.execute('select * from questions where statement like ? order by id desc limit 10', [excerpt])
        result = cursor.fetchall()
        return [Question(row[1], row[2], row[0]) for row in result]

def find_by_id(id: int) -> Question | None:
    with connection:
        cursor = connection.cursor()
        cursor.execute(
            'select * from questions inner join alternatives on alternatives.question_id = questions.id ' +
            'where questions.id = ?',
            [id]
        )
        result = cursor.fetchall()
        alternatives = [Alternative(row[4], row[5], row[6], row[3]) for row in result]
        return Question(result[0][1], result[0][2], result[0][0], alternatives)

def find_by_subject_id(subject_id: int) -> list[Question]:
    with connection:
        cursor = connection.cursor()
        cursor.execute(
            'select * from questions inner join alternatives on questions.id = alternatives.question_id ' +
            'where subject_id = ?',
            [subject_id]
        )
        result = cursor.fetchall()
        alternatives: list[Alternative] = []
        questions: list[Question] = []
        lastrow = -1
        for i, row in enumerate(result):
            if i > 0 and row[0] != result[lastrow][0]:
                questions.append(Question(result[lastrow][1], result[lastrow][2], result[lastrow][0], alternatives))
                alternatives = []
            alternatives.append(Alternative(row[4], row[5], row[6], row[3]))
            lastrow = i
        questions.append(Question(result[lastrow][1], result[lastrow][2], result[lastrow][0], alternatives))
        return questions

def insert(question: Question) -> int | None:
    with connection:
        cursor = connection.cursor()
        cursor.execute(
            'insert into questions (statement, subject_id) values (?, ?)',
            [question.statement, question.subject_id]
        )
        return cursor.lastrowid

def update(question: Question) -> None:
    with connection:
        connection.execute(
            'update questions set statement = ?, subject_id = ? where id = ?',
            [question.statement, question.subject_id, question.id]
        )