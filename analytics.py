def plot_expense_summary(db_path="data/expenses.db"):
    pass

def backup_to_csv(db_path="data/expenses.db"):
    with sqlite3.connect(db_path) as conn:
        data_frame = pd.read_sql_query("SELECT * FROM expenses", conn)
        data_frame.to_csv("data/expenses_backup.csv", index=False)
