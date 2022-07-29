from . import create_session

class CRUDUser:

    @staticmethod
    @create_session
    def add(
            login: int,
            password: str,
            email: str,
            role_id: int,
            cur=None,
            conn=None
    ) -> None:
        cur.execute("""
            INSERT INTO users(login, password, email, role_id) 
            VALUES(?, ?, ?, ?);
        """, (login, password, email, role_id))
        conn.commit()