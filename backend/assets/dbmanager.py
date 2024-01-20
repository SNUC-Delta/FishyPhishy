import sqlite3

class DBManager:
    # singleton class
    instance = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DBManager, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.conn = sqlite3.connect('db.sqlite3')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def create_table(self):
        # todo: need to rethink the columns
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
        );
        """)
        self.conn.commit()

    def insert(self, url: str):
        # if url isnt already in the db
        # then add only those urls to the db
        #