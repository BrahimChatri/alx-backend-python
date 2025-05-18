seed = __import__('seed')


def stream_user_ages():
    """Generator that yields user ages one by one."""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")

    for row in cursor:
        yield row['age']

    connection.close()


def average_user_age():
    """Calculate and print the average user age using the age generator."""
    total_age = 0
    count = 0

    for age in stream_user_ages():
        total_age += age
        count += 1

    if count > 0:
        average = total_age / count
        print(f"Average age of users: {average}")
    else:
        print("No users found.")
