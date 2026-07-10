import sqlite3
import os
from config import DATABASE_PATH, ADMIN_USERNAME, ADMIN_PASSWORD


def get_db_connection():
    """
    Creates and returns a SQLite connection.
    """
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
    Creates database and tables if they don't exist.
    Also inserts the default admin user.
    """

    # Create database folder if missing
    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)

    conn = get_db_connection()
    cursor = conn.cursor()

    # ==========================
    # Users Table
    # ==========================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # ==========================
    # Tasks Table
    # ==========================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            task TEXT NOT NULL,

            assigned_to TEXT NOT NULL,

            priority TEXT NOT NULL,

            deadline TEXT NOT NULL,

            description TEXT,

            status TEXT NOT NULL,

            completed INTEGER DEFAULT 0,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # ==========================
    # Insert Default Admin
    # ==========================
    cursor.execute(
        "SELECT * FROM users WHERE username = ?",
        (ADMIN_USERNAME,)
    )

    user = cursor.fetchone()

    if user is None:
        cursor.execute(
            """
            INSERT INTO users(username, password)
            VALUES (?, ?)
            """,
            (ADMIN_USERNAME, ADMIN_PASSWORD)
        )

    conn.commit()
    conn.close()