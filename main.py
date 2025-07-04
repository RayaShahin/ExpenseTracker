from db import init_db
from tracker import add_expense, remove_expense, list_expense, remove_all_expense
from analytics import plot_expense_summary, backup_to_csv
    
def get_budget_limit():
    try:
        limit = float(input("Set your monthly budget limit: "))
        return limit
    except ValueError:
        print("❌ Invalid number. Using default: 2000")
        return 2000

# set monthly limit
budget_limit = get_budget_limit()

def budget_warning(db_path="data/expenses.db"):
    from datetime import datetime
    import sqlite3
    
    current_datetime = datetime.now()
    month = current_datetime.strftime("%Y-%m")
    
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        # get the sum of the amount spent to see if it exceeds budget limit
        c.execute("SELECT SUM(amount) FROM expenses WHERE date LIKE ?", (f"{month}%",))
        # retrieve the result of the query and if no matching rows are found, return None or 0
        total = c.fetchone()[0] or 0 # This ensures the app does not crash
    
    if total > budget_limit:
        print(f"⚠️ WARNING: Monthly spending exceeded! (Total: {total})")

def show_menu():
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. Remove Expense")
    print("3. View Expenses")
    print("4. Remove All Expenses")
    print("5. Show Monthly Summary")
    print("6. Exit")
    
if __name__ == "__main__":
    # initialize database
    init_db()
    print("✅ Database initialized successfully!")
    while True:
        show_menu()
        option = input("\nEnter Option: ")
        if option == "1":
            try:
                amount = float(input("Amount: "))
                category = input("Category: ")
                note = input("Note (optional): ")
                add_expense(amount, category, note)
                budget_warning()
            except ValueError:
                print("❌ Invalid amount. Please enter a number.")
        elif option == "2":
            expense_id = input("Expense ID: ")
            # confim before deleting
            confirm = input(f"Are you sure you want to delete expense with ID {expense_id}? (yes/no): ")
            if confirm.lower() == "yes" and expense_id.isdigit():
                remove_expense(int(expense_id))
            else:
                print("❌ Invalid ID. Must be a number.")
        elif option =="3":
            rows = list_expense()
            if not rows:
                print("No expenses found.")
            else:
                for row in rows:
                    print(row)
        elif option == "4":
            # confim before deleting
            confirm = input("Are you sure you want to delete all expenses? (yes/no): ")
            if confirm.lower() == "yes":
                remove_all_expense()
        elif option == "5":
            plot_expense_summary()
        elif option == "6":
            backup_to_csv()
            print("📁 Backup created. Exiting...")
            break
        else:
            print("❌ Invalid option.")
