import sqlite3
import os

DB_PATH = os.path.join("data", 'document.db')

def get_db_connection():
    return sqlite3.connect(DB_PATH)  # Connect to the SQLite database


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Documents table to store document
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT ,
            path TEXT ,
            thumbnail_path TEXT,
            tags TEXT,
            description TEXT ,
            uploaded_date text ,
            lecture_name TEXT ,
            lecture_date TEXT ,
            total_pages INTEGER ,
            last_accessed_date text
        )
    ''')
    
    conn.commit()
    print("Database initialized successfully.")
    cursor.close()
    conn.close()
    