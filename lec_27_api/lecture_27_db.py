import sqlite3
from sqlite3 import Error


db = "flask_db.sqlite"


def create_conn():
    db_conn = None
    try:
        db_conn = sqlite3.connect(db)
    except Error as e:
        print(e)
    return db_conn


def create_table(sql_query):
    db_conn = create_conn()
    try:
        c = db_conn.cursor()
        c.execute(sql_query)
        db_conn.close()
    except Error as e:
        print(e)


def main():
    sql_create_groups = """CREATE TABLE users (
                            id INTEGER,
                            name TEXT,
                            login TEXT,
                            password TEXT,
                            PRIMARY KEY(id ASC)
                        ); """

    db_conn = create_conn()

    if db_conn is not None:
        create_table(sql_create_groups)


def create_user(name, login, password):
    sql_query = (f"INSERT INTO users (name,login,password) "
                 f"VALUES ('{name}','{login}','{password}');")
    db_conn = create_conn()
    c = db_conn.cursor()
    c.execute(sql_query)
    db_conn.commit()
    db_conn.close()
    return c.lastrowid


def check_user(login, password):
    db_conn = create_conn()
    c = db_conn.cursor()
    c.execute(f"SELECT id, name FROM users "
              f"WHERE login='{login}' AND password='{password}';")
    user = c.fetchone()
    db_conn.close()
    return user


if __name__ == '__main__':
    main()
    last_id = create_user('john', 'jjj1', 'dfsdff')
    print(last_id)
