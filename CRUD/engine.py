import psycopg2

def create_session(func):
    def wrapper(**kwargs):
        conn = psycopg2.connect("postgresql://Alesya:15121980Fktcz@localhost:5432/postgres")
        cur = conn.cursor()
        return func(**kwargs, cur=cur, conn=conn)
    return wrapper