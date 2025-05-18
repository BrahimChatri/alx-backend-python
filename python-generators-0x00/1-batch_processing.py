#!/usr/bin/python3
seed = __import__('seed')


def stream_users_in_batches(batch_size):
    """Generator to yield users in batches from the database."""
    offset = 0

    while True:
        connection = seed.connect_to_prodev()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM user_data LIMIT {batch_size} OFFSET {offset}")
        rows = cursor.fetchall()
        connection.close()

        if not rows:
            return

        yield rows
        offset += batch_size


def batch_processing(batch_size):
    """Process each batch, filter users over age 25, and print them."""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)
