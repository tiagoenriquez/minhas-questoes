definition = """
create table if not exists disciplinas (
    id integer not null primary key,
    nome varchar (32) not null unique
)
"""