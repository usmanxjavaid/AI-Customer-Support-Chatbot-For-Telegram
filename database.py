import sqlite3
from datetime import datetime

# Connect to database file (create it if it dooesn't exist)
DB_FILE = 'databse.db'

# define a function which creates a connection with sqlite3 database
def get_connection():
    conn = sqlite3.connect(DB_FILE)
    return conn

def init_db():
    """
    Creates table if they don't exist yet.
    Runs once when bot starts.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            telegram_id INTEGER UNIQUE,
            first_name TEXT,
            username TEXT,
            joined_at TEXT
        )
    ''')

    # Create conversations table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY,
            telegram_id INTEGER,
            role TEXT,
            message TEXT,
            timestamp TEXT
        )
    ''')

    conn.commit()
    conn.close()

def save_user(telegram_id: int, first_name: str, username: str):
    """
    Saves users to users table in database.
    If user already exists, update their info.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT OR IGNORE INTO users (telegram_id, first_name, username, joined_at)
    VAlUES (?, ?, ?, ?)
    ''', (telegram_id, first_name, username, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    conn.commit()
    conn.close()

def save_message(telegram_id: int, role: str, message: str):
    """
    Saves every message to conversation table in database.
    role = 'user' or 'assistant'
    """

    conn =get_connection()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO conversations (telegram_id, role, message, timestamp)
    VALUES (?, ?, ?, ?)
    ''', (telegram_id, role, message, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    conn.commit()
    conn.close()

def get_all_users():
    """Returns list of all users"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT telegram_id, first_name, username, joined_at FROM users')
    users = cursor.fetchall()
    conn.close()
    return users

def get_user_conversations(telegram_id: int):
    """Returns all messages for a specific user"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT role, message, 
        timestamp FROM conversations
        WHERE telegram_id = ?
        ORDER BY timestamp ASC
        ''', (telegram_id,))
    messages = cursor.fetchall()
    conn.close()
    return messages

def get_stats():
    """Return basic stats for admin panel"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM users')
    total_users = cursor.fetchone()[0]

    cursor.execute('SELECT COUNT(*) FROM conversations')
    total_messages = cursor.fetchone()[0]

    conn.close()
    return total_users, total_messages


# you can use below command to check number of users and messages (e.g. (1,4))
# python -c "import database; print(database.get_stats())"





