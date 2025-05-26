import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def __enter__(self):
        # Open the connection and create cursor
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        # Commit any changes and close connection
        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()

# Usage example
if __name__ == "__main__":
    db_file = "example.db"  # Change to your database file or connection string

    # Assuming a table 'users' exists in your database
    with DatabaseConnection(db_file) as cursor:
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        for row in results:
            print(row)
