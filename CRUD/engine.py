import psycopg2


def create_session(func):
    def wrapper(**kwargs):
        conn = psycopg2.connect("postgresql://postgres:15121980Fktcz@localhost:5432/bh57")
        cur = conn.cursor()
        return func(**kwargs, cur=cur, conn=conn)
    return wrapper


@create_session
def create_table(cur=None, conn=None):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS categories(
            id INTEGER PRIMARY KEY,
            name VARCHAR(24)
        );
    """)


@create_session
def create_table(cur=None, conn=None):
    cur.execute("""
        CREATE TABLE if NOT EXISTS categories(
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL
        );
    """)

@create_session
def create_table(cur=None, conn=None):
    cur.execute("""
        CREATE TABLE if NOT EXISTS roles(
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL
    );
""")

@create_session
def create_table(cur=None, conn=None):
    cur.execute("""
        CREATE TABLE if NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            login TEXT UNIQUE NOT NULL,
            password TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            role_id INTEGER NOT NULL,
            FOREIGN KEY (role_id) REFERENCES roles(id)
    );
""")

@create_session
def create_table(cur=None, conn=None):
    cur.execute("""
        CREATE TABLE if NOT EXISTS articles(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            body TEXT NOT NULL,
            category_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (category_id) REFERENCES categories(id),
            FOREIGN KEY (user_id) REFERENCES users(id)
    );
""")

    conn.commit()

create_table()