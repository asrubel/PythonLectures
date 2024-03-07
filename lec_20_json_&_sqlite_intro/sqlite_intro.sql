CREATE TABLE groups (
    id INTEGER,
    title TEXT,
    PRIMARY KEY(id ASC)
);

INSERT INTO groups (title) VALUES ('518');

INSERT INTO groups (title)
VALUES
    ('519'),
    ('519st'),
    ('518st');

SELECT * FROM groups;

SELECT title FROM groups;

SELECT * FROM groups
WHERE id > 2;

SELECT * FROM groups
WHERE title='519';

SELECT * FROM groups
WHERE title LIKE '51%';

SELECT * FROM groups
WHERE title LIKE '%st';

INSERT INTO groups (title) VALUES ('619a');

UPDATE groups
SET title = '519a'
WHERE id = 5;

BEGIN TRANSACTION;

SELECT * FROM groups;

UPDATE groups
SET title = '519a';

SELECT * FROM groups;

ROLLBACK;

SELECT * FROM groups;
