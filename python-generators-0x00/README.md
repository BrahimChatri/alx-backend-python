# python-generators-0x00

## 📌 Project Overview

This project demonstrates the use of **Python generators** to efficiently stream data from a MySQL database. It also includes a setup script to create and populate a database with user data, showcasing best practices in database interaction and data processing.

---

## 🚀 Features

- ✅ MySQL database setup and connection
- ✅ Creation of a `user_data` table with the required fields
- ✅ Data import from `user_data.csv` file
- ✅ Use of generators to fetch rows one at a time
- ✅ Follows clean and modular function design
- ✅ Efficient and scalable data handling

---

## 🗃️ Database Schema

**Database**: `ALX_prodev`  
**Table**: `user_data`

| Column    | Type       | Description                     |
|-----------|------------|---------------------------------|
| user_id   | UUID       | Primary Key, unique identifier |
| name      | VARCHAR    | Full name of the user          |
| email     | VARCHAR    | User's email address           |
| age       | DECIMAL    | User's age                     |

---

## 📂 File Structure

```

python-generators-0x00/
├── 0-main.py           # Main script to run setup functions
├── seed.py             # Database connection, creation, and CSV data insertion
├── user\_data.csv       # Sample dataset to be imported
├── README.md           # Project documentation

````

---

## 🔧 Usage

1. **Make sure MySQL server is running.**
2. **Run the setup:**

```bash
./0-main.py
````

3. If everything is correct, it will:

   * Connect to MySQL
   * Create the `ALX_prodev` database and `user_data` table
   * Import data from `user_data.csv`
   * Output sample data to confirm successful setup

---

## 📦 Functions in `seed.py`

* `connect_db()` – Connects to MySQL server.
* `create_database(connection)` – Creates the `ALX_prodev` database if it doesn’t exist.
* `connect_to_prodev()` – Connects directly to `ALX_prodev`.
* `create_table(connection)` – Creates the `user_data` table if it doesn’t exist.
* `insert_data(connection, data)` – Inserts CSV data into the table if not already present.

---

## ⚠️ Notes

* Update the MySQL username/password in `seed.py` as needed.
* Add sensitive files like `.env` to `.gitignore` to avoid accidentally pushing them to GitHub.

---

## ✅ Example Output

```
connection successful
Table user_data created successfully
Database ALX_prodev is present 
[('00234e50...', 'Dan Altenwerth Jr.', 'Molly59@gmail.com', 67), ...]
```

---

## 🧠 Author

Created as part of the ALX Backend Specialization – Python Generators project.

```
