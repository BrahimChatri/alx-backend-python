import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def stream_users():
    # Connect to the database
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database="ALX_prodev"
    )

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    # Generator: Yield one row at a time
    for row in cursor:
        yield row

    # Cleanup
    cursor.close()
    connection.close()
