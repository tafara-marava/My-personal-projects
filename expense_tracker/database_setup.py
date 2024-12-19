import sqlite3

def setup_database():
    connection = sqlite3.connect('expense_tracker.db')
    cursor = connection.cursor()
    
    # Create expenses table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        description TEXT
    )
    ''')
    
    connection.commit()
    connection.close()
    print("Database and table created successfully.")

if __name__ == '__main__':
    setup_database()
