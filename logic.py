import sqlite3
from bot import user_request
from config import DATABASE

class DB_Manager:
    def __init__(self, database):
        self.database = database
        
    def select(self):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute(f'''SELECT * FROM data WHERE Name LIKE "{user_request}%"
                        ''')
            return cur.fetchall()

    def __executemany(self, sql, data):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.executemany(sql, data)
            conn.commit()
    
    def __select_data(self, sql, data = tuple()):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute(sql, data)
            return cur.fetchall()
            
if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
