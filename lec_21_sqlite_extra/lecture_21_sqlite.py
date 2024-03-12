import sqlite3
from sqlite3 import Error


def create_conn(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(type(conn))
        print(sqlite3.version)
    except Error as e:
        print(e)
    # finally:
    #     if conn:
    #         conn.close()
    return conn


def create_table(conn, sql_query):
    try:
        c = conn.cursor()
        c.execute(sql_query)
    except Error as e:
        print(e)


def main():
    db = "my_db.sqlite"

    sql_create_groups = """CREATE TABLE groups (
                            id INTEGER,
                            title TEXT,
                            PRIMARY KEY(id ASC)
                        ); """

    conn = create_conn(db)

    if conn is not None:
        create_table(conn, sql_create_groups)


def create_group(conn, group_title):
    sql_query = f"INSERT INTO groups (title) VALUES ('{group_title}');"
    c = conn.cursor()
    c.execute(sql_query)
    conn.commit()
    return c.lastrowid


def get_all_groups(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM groups ORDER BY title DESC;")
    rows = c.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    # create_conn("my_db.sqlite")
    # main()
    conn = create_conn("my_db.sqlite")
    with conn:
        last_id = create_group(conn, '549')
        print(last_id)
        get_all_groups(conn)
