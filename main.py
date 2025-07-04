from db import init_db
from tracker import add_expense, remove_expense, list_expense, remove_all_expense
from analytics import plot_expense_summary, backup_to_csv
    
def get_budget_limit():
    pass

# set monthly limit
budget_limit = get_budget_limit()

def budget_warning(db_path="data/expenses.db"):
    pass

def show_menu():
    pass

if __name__ == "__main__":
    # initialize database
    init_db()
    print("✅ Database initialized successfully!")
    
    while True:
        pass
