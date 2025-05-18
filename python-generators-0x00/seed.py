import mysql.connector
import csv
import uuid

# 1. Connect to MySQL server (default connection, no specific DB)
def connect_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'  # Replace with your actual password
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# 2. Create ALX_prodev database if not exists
def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
    cursor.close()

# 3. Connect specifically to ALX_prodev database
def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password',  # Replace with your actual password
            database='ALX_prodev'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# 4. Create table user_data
def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL(5,2) NOT NULL
        );
    """)
    connection.commit()
    cursor.close()
    print("Table user_data created successfully")

# 5. Insert data from CSV
def insert_data(connection, file_path):
    cursor = connection.cursor()
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            user_id = row['user_id']
            name = row['name']
            email = row['email']
            age = row['age']

            # Check if user already exists
            cursor.execute("SELECT * FROM user_data WHERE user_id = %s", (user_id,))
            if cursor.fetchone():
                continue

            cursor.execute(
                "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                (user_id, name, email, age)
            )
    connection.commit()
    cursor.close()
