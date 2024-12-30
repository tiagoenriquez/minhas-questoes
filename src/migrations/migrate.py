from src.connections.DatabaseConnection import con
from src.migrations import AlternativaMigration, DisciplinaMigration, QuestaoMigration


def migrate():
    with con:
        con.execute(DisciplinaMigration.definition)
        con.execute(QuestaoMigration.definition)
        con.execute(AlternativaMigration.definition)
        con.commit()