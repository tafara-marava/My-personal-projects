import sqlite3

DATABASE = 'expense_tracker.db'

def create_table():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            date TEXT,
            amount REAL,
            category TEXT,
            description TEXT
        )
    ''')
    connection.commit()
    connection.close()

def add_expense(date, amount, category, description):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute('''
    INSERT INTO expenses (date, amount, category, description)
    VALUES (?, ?, ?, ?)
    ''', (date, amount, category, description))
    connection.commit()
    connection.close()

def view_expenses():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM expenses')
    rows = cursor.fetchall()
    connection.close()
    return rows

def update_expense(expense_id, date, amount, category, description):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute('''
    UPDATE expenses
    SET date = ?, amount = ?, category = ?, description = ?
    WHERE id = ?
    ''', (date, amount, category, description, expense_id))
    connection.commit()
    connection.close()

def delete_expense(expense_id):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
    connection.commit()
    connection.close()

def summarize_expenses():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute('''
    SELECT category, SUM(amount) as total
    FROM expenses
    GROUP BY category
    ORDER BY total DESC
    ''')
    summary = cursor.fetchall()
    connection.close()
    return summary

# Call create_table() at the start of your script
create_table()
