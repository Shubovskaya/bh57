from engine import create_session

class CRUDCategory:

    @staticmethod
    @create_session
    def add(name: str, cur=None, conn=None) -> None:
        cur.execute("""
            INSERT INTO categories(name)
            VALUES(?);
        """, (name, ))
        conn.commit()

CRUDCategory.add(name="auto")

# conn = sqlite3.connect("db.db")
# cur = conn.cursor()
# cur.execute("""
#     CREATE TABLE IF NOT EXISTS categories(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name VARCHAR(45) NOT NULL
#     );
# """)
# cur.execute("""
#     CREATE TABLE IF NOT EXISTS roles(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name VARCHAR(45) NOT NULL
#     );
# """)
#
# cur.execute("""
#     CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     login VARCHAR(45) NOT NULL,
#     password VARCHAR(50) NOT NULL,
#     email VARCHAR(45),
#     role_id INTEGER NOT NULL,
#     FOREIGN KEY (role_id) REFERENCES roles(id)
#     );
# """)
#
# cur.execute("""
#     CREATE TABLE IF NOT EXISTS articles(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title VARCHAR(45) NOT NULL,
#     body VARCHAR(3000) NOT NULL,
#     category_id INTEGER NOT NULL,
#     users_id INTEGER NOT NULL,
#     FOREIGN KEY (category_id) REFERENCES categories(id)
#     FOREIGN KEY (users_id) REFERENCES users(id)
#     );
# """)
#
# conn.commit()

