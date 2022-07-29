from .engine import create_session

class CRUDRole:

    @staticmethod
    @create_session
    def add(name: str, cur=None, conn=None) -> None:
        cur.execute("""
            INSERT INTO categories(name)
            VALUES(?);
        """, (name, ))
        conn.commit()


