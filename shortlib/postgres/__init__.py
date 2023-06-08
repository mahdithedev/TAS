import psycopg2
from shortlib.repository import Repository

# Implmentation of Repository for postgres

class PostgresRepo(Repository):

    def __init__(self , address) -> None:
        self.conn = psycopg2.connect(address)
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    def save(self, url, new):
        query = f"""INSERT INTO URLS (New , Original) 
        VALUES (%s , %s);"""
        self.cur.execute(query , (new , url))

    def get(self , url):
        query = f"SELECT * FROM URLS WHERE new=\'{url}\'"
        self.cur.execute(query)
        return self.cur.fetchall()[0]
    
    def click(self , url):
        query = f"UPDATE URLS SET ClickCount = ClickCount + 1 WHERE Original=\'{url}\'"
    
    def __del__(self):
        self.conn.close()