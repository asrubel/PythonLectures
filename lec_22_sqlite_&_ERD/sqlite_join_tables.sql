CREATE TABLE students (
    student_id INTEGER,
    first_name TEXT,
    last_name TEXT,
    group_id INTEGER,
    PRIMARY KEY(student_id ASC),
    FOREIGN KEY (group_id) REFERENCES groups(id)
);

INSERT INTO students (first_name, last_name, group_id)
VALUES
    ('Ivan', 'Shevchenko', 1),
    ('Ivan', 'Shevchenko', 2),
    ('Oleh', 'Ivanenko', 1),
    ('Olha', 'Shevchuk', 3),
    ('Oleksandr', 'Korovnichenko', 2),
    ('Violetta', 'Ilyina', 1),
    ('Maksym', 'Besedin', 3);

SELECT * FROM students;

SELECT * FROM students s
JOIN groups g on g.id = s.group_id;

SELECT s.first_name, s.last_name, g.title
FROM students s
JOIN groups g on g.id = s.group_id
ORDER BY g.id;
