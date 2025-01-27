alternative_definition = """
create table alternatives (
    id integer not null primary key autoincrement,
    alternative_text text,
    correct boolean not null,
    question_id interger not null,
    foreign key (question_id) references questions (id)
)
"""