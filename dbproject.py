import sqlite3

DATABASE_NAME = 'students.db'

def connect_database():
    """connect to the database and enable foreign key"""
    connection = sqlite3connect(DATABASE_NAME)
    connection.execute("PRAGMA Foreign_keys = ON")
    return connection

def create_tables():
    """Create the students table if it does not exist"""
    with connect_database()