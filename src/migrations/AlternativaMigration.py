definition = """
create table if not exists alternativas (
    id integer not null primary key,
    texto text not null,
    correto boolean not null,
    questao_id integer not null,
    foreign key (questao_id) references questoes(id)
)
"""