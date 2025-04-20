question_definition = """
create table questions (
    id integer not null primary key autoincrement,
    statement text,
    subject_id integer not null,
    foreign key (subject_id) references subjects (id) on delete cascade
)
"""