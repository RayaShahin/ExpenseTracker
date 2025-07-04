import sqlite3
from pathlib import Path

db_path = "data/expenses.db"

def init_db():
    # constructs a Path object ("data" folder)
    Path("data").mkdir(exist_ok=True) # ensures whether or not "data" folder exists
    
    with sqlite3.connect(db_path) as conn: # open connection to database and closes it automatically
        c = conn.cursor() # create cursor object to execute SQL commands
        
        # to start the id count from 1 each time ite generated
        c.execute("DROP TABLE IF EXISTS expenses")
        
        # execute query to create table if not exists
        c.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            note TEXT
            )
        ''')
        conn.commit() # commit changes
        c.close() # close cursor
         