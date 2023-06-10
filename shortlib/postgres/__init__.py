import psycopg2
from shortlib.repository import Repository
from datetime import date

# Implmentation of Repository for postgres

class PostgresRepo(Repository):

    def __init__(self , address = "" , conn = None) -> None:
        if address:
            self.conn = psycopg2.connect(address)
        elif conn:
            self.conn = conn
        else:
            raise Exception("could'nt open a connection with postgres databse beacuse (address and conn are None)")
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    def create(self , url , new , owner_ID , owner_channel , lifetime):
        query = f"""INSERT INTO URLS (New , Original , OwnerID , OwnerChannel , Lifetime , CreatedAt) 
        VALUES (%s , %s , %s , %s , %s , %s);"""
        today = date.today()
        self.cur.execute(query , (new, url, owner_ID, owner_channel , lifetime , today))

    def read(self , url):
        query = f"SELECT * FROM URLS WHERE new=\'{url}\'"
        self.cur.execute(query)
        return self.cur.fetchall()[0]
    
    def update(self):
        return super().update()
    
    def delete(self):
        return super().delete()
    
    def click(self , url):
        query = f"UPDATE URLS SET ClickCount = ClickCount + 1 WHERE Original=\'{url}\'"

    # This is not any borrowing mechanism and is purly a function name
    def borrow_connection(self):
        return self.conn
    
    def __del__(self):
        self.conn.close()