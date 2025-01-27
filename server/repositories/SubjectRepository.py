from server.connections.DatabaseConnection import connection
from server.models.Subject import Subject


def all() -> list[Subject]:
    with connection:
        cursor = connection.cursor()
        cursor.execute('select * from subjects order by name')
        result = cursor.fetchall()
        subjects: list[Subject] = []
        [subjects.append(Subject(row[1], row[0])) for row in result]
        return subjects

def count() -> int:
    with connection:
        cursor = connection.cursor()
        cursor.execute('select count(*) from subjects')
        return cursor.fetchone()

def delete(id: int) -> None:
    with connection:
        connection.execute('delete from subjects where id = ?', [id])
        connection.commit()

def find(id: int) -> Subject | None:
    with connection:
        cursor = connection.cursor()
        cursor.execute('select * from subjects where id = ?', [id])
        result = cursor.fetchone()
        if not result:
            return None
        return Subject(result[1], result[0])

def find_by_name(name: str) -> Subject | None:
    with connection:
        cursor = connection.cursor()
        cursor.execute('select * from subjects where name = ?', [name])
        result = cursor.fetchone()
        if not result:
            return None
        return Subject(result[1], result[0])

def insert(subject: Subject) -> None:
    with connection:
        connection.execute('insert into subjects (name) values (?)', [subject.name])
        connection.commit()

def update(subject: Subject) -> None:
    with connection:
        connection.execute('update subjects set name = ? where id = ?', [subject.name, subject.id])
        connection.commit()

def with_n_questions() -> list[Subject]:
    with connection:
        cursor = connection.cursor()
        cursor.execute(
            'select *, count(questions.subject_id) as n_questions from subjects ' +
            'inner join questions on subjects.id = questions.subject_id ' +
            'group by subjects.name order by n_questions desc'
        )
        result = cursor.fetchall()
        return [Subject(row[1], row[0], row[5]) for row in result]
