from engine import create_session


class CRUDArticle:

    @staticmethod
    @create_session
    def add(
            title: str,
            body: str,
            category_id: int,
            user_id: int,
            cur=None,
            conn=None
    ) -> None:
        cur.execute("""
            INSERT INTO articles(title, body, category_id, user_id) 
            VALUES(?, ?, ?, ?);
        """, (title, body, category_id, user_id))
        conn.commit()
