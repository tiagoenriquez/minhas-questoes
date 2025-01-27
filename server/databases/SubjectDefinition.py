subject_definition = """
create table subjects (
    id integer not null primary key autoincrement,
    name varchar (63) not null unique
)
"""