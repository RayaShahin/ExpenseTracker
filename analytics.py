import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def plot_expense_summary(db_path="data/expenses.db"):
    with sqlite3.connect(db_path) as conn:
        # retrieving the data from the database as a DataFrame
        data_frame = pd.read_sql_query("SELECT * FROM expenses", conn)
        
    # checks if the DataFrame is empty or not 
    if data_frame.empty:
        print("No data to visualize.")
        return
    
    # convert "date" column to datetime and extract month
    data_frame["date"] = pd.to_datetime(data_frame["date"])
    data_frame["month"] = data_frame["date"].dt.to_period("M") 
    
    # plotting the monthly expenses
    monthly = data_frame.groupby("month")["amount"].sum()
    monthly.plot(kind="bar", title="Monthly Expenses")
    plt.xlabel("Month")
    plt.ylabel("Total Amount")
    plt.tight_layout()
    plt.savefig("plots/monthly_expenses.png")
    plt.show()

def backup_to_csv(db_path="data/expenses.db"):
    with sqlite3.connect(db_path) as conn:
        data_frame = pd.read_sql_query("SELECT * FROM expenses", conn)
        data_frame.to_csv("data/expenses_backup.csv", index=False)
