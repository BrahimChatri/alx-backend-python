import asyncio
import aiosqlite

DB_FILE = "example.db"  # Replace with your actual database file

async def async_fetch_users():
    async with aiosqlite.connect(DB_FILE) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            users = await cursor.fetchall()
            return users

async def async_fetch_older_users():
    async with aiosqlite.connect(DB_FILE) as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            older_users = await cursor.fetchall()
            return older_users

async def fetch_concurrently():
    # Run both queries concurrently
    all_users, users_over_40 = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    
    print("All users:")
    for user in all_users:
        print(user)

    print("\nUsers older than 40:")
    for user in users_over_40:
        print(user)

if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
