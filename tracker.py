import sqlite3
from datetime import datetime

def add_expense(amount, category, note="", db_path="data/expenses.db"):
    
    # validate inputs
    if not isinstance(amount, (int, float)) or amount <= 0:
        raise ValueError("Amount must be a positive number.")
    if not isinstance(category, str) or not category:
        raise ValueError("Category must be a non-empty string.")
    if note and not isinstance(note, str):
        raise ValueError("Note must be a string.")
    
    # get the current date and time formatted as YYYY-MM-DD
    expense_date = datetime.now().strftime("%Y-%m-%d")
    
    try:
        with sqlite3.connect(db_path) as conn:
            c = conn.cursor()
            
            # insert expense data into the expenses table
            c.execute('INSERT INTO expenses (amount, category, date, note) VALUES (?, ?, ?, ?)', # using a parameterized query to prevent SQL injection
                    (amount, category, expense_date, note))
            conn.commit()
            print("✅ Expense added successfully!")
            
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        
def remove_expense(id, db_path="data/expenses.db"):
    try:
        with sqlite3.connect(db_path) as conn:
            c = conn.cursor()
            
            # check whether or not the expense exists
            c.execute("SELECT * FROM expenses WHERE id = ?", (id,))
            if c.fetchone() is None:
                print(f"No expense found with ID {id}.")
                return
            
            # delete the expense
            c.execute("DELETE FROM expenses WHERE id = ?", (id,))
            conn.commit()
            print(f"Expense with ID {id} removed successfully!")  
              
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def list_expense(db_path="data/expenses.db"):
    try:
        with sqlite3.connect(db_path) as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM expenses ORDER BY date DESC")
            # retrieve the rows from the the query
            rows = c.fetchall()
        return rows
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

def remove_all_expense(db_path="data/expenses.db"):
    try:
        with sqlite3.connect(db_path) as conn:
            c = conn.cursor()
            
            # delete all expenses
            c.execute("DELETE FROM expenses")
            conn.commit()
            print(f"All expenses successfully removed!")  
              
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}") 
