import psycopg2
from shortlib.repository import ShortRepository
from datetime import date
import time

# Implmentation of Repository for postgres

class PostgresRepo(ShortRepository):

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
        query = f"""INSERT INTO URLS (New , Original , OwnerID , OwnerChannel , Lifetime) 
        VALUES (%s , %s , %s , %s , %s);"""
        self.cur.execute(query , (new, url, owner_ID, owner_channel , lifetime))

    def read(self , url):
        query = f"SELECT * FROM URLS WHERE new=\'{url}\'"
        self.cur.execute(query)
        return self.cur.fetchall()[0]
    
    def update(self):
        return super().update()
    
    def delete(self):
        return super().delete()
    
    def click(self, url, IP, user_agent):
        query = "INSERT INTO Clicks (URL, IPV4, UserAgent) VALUES (%s, %s, %s)"
        try:
            self.cur.execute(query , (url , IP , user_agent))
            return True
        except Exception as e:
            return False

    def read_and_click(self, url, IP, user_agent):
        return super().read_and_click(url, IP, user_agent)

    # This is not any borrowing mechanism and is purly a function name
    def borrow_connection(self):
        return self.conn
    
    def __del__(self):
        self.conn.close()