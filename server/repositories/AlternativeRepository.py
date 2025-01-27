from server.connections.DatabaseConnection import connection
from server.models.Alternative import Alternative


def delete(question_id: id) -> None:
    with connection:
        connection.execute('delete from alternatives where question_id = ?', [question_id])

def insert(alternatives: list[Alternative], question_id: int) -> None:
    data = [(alternative.alternative_text, alternative.correct, question_id) for alternative in alternatives]
    with connection:
        connection.executemany(
            'insert into alternatives (alternative_text, correct, question_id) values (?, ?, ?)',
            data
        )
        connection.commit()

def update(alternatives: list[Alternative]) -> None:
    data = []
    for alternative in alternatives:
        data.append((alternative.alternative_text, alternative.correct, alternative.question_id, alternative.id))
    with connection:
        connection.executemany(
            'update alternatives set alternative_text = ?, correct = ?, question_id = ? where id = ?',
            data
        )
        connection.commit()