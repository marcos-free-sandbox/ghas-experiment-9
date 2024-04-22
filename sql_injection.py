import sqlite3

def get_user(username):
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()

    # Unsafe query
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    result = cursor.fetchone()

    return result
