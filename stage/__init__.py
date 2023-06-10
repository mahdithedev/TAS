import psycopg2
import numpy as np

# stage only works with postgres for now
class Stage():

    def __init__(self , address = "" , conn = None) -> None:
        if address:
            self.conn = psycopg2.connect(address)
        elif conn:
            self.conn = conn
        else:
            raise Exception("could'nt open a connection with postgres databse beacuse (address and conn are None)")
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    def get_query(self , category_evaluation: dict):
        query = "INSERT INTO Stage"
        if category_evaluation == {}:
            category_evaluation["fun"] = 0
        fields = "".join(map(lambda x: f"{x}, " , category_evaluation))
        fields = fields[:-2]
        values = "%s, "*len(category_evaluation)
        values = values[:-2]
        query += f" (URL, {fields}) VALUES (%s, {values});"
        return query

    def create(self , url , category_evaluation: dict):
        # prepare the query
        query = self.get_query(category_evaluation)
        self.cur.execute(query , tuple([url]) + tuple(category_evaluation.values()))

    def read(self):
        return super().read()
    
    def read_all(self):
        self.cur.execute("SELECT * FROM Stage;")
        return self.cur.fetchall()

    def update(self):
        return super().update()
    
    def delete(self , url):
        self.cur.execute("DELETE FROM Stage WHERE URL=%1" , (url))
    
    # This is not any borrowing mechanism and is purly a function name
    def borrow_connection(self):
        return self.conn
    
    def __del__(self):
        self.conn.close()
    
    def score(self , vector):
        stage_urls = self.read_all()
        t = list(map(lambda x: x[1:] , stage_urls))
        values = np.array(t)
        result = values.dot(vector)
        return (stage_urls , result)
