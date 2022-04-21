create table users (
    id SERIAL PRIMARY KEY ,
    name TEXT NOT NULL,
    password TEXT NOT NULL,
    expert BOOLEAN NOT NULL,
    admin BOOLEAN NOT NULL
);

create table questions (
    id SERIAL PRIMARY KEY ,
    question_text TEXT NOT NULL,
    answer_text TEXT,
    asked_by_id INTEGER NOT NULL,
    expert_id INTEGER NOT NULL
);