from server.connections.DatabaseConnection import connection
from server.databases.AlternativeDefinition import alternative_definition
from server.databases.QuestionDefinition import question_definition
from server.databases.SubjectDefinition import subject_definition


with connection:
    cursor = connection.cursor()
    cursor.execute(subject_definition)
    cursor.execute(question_definition)
    cursor.execute(alternative_definition)