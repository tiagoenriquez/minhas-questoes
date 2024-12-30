definition = """
create table if not exists questoes (
    id integer not null primary key,
    enunciado text not null,
    disciplina_id integer not null,
    foreign key (disciplina_id) references disciplinas(id)
)
"""