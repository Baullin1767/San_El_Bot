import sqlite3
import time

connect = sqlite3.connect("database.db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id INT,
    username TEXT,
    name TEXT,
    status TEXT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS cods(
    cod TEXT
)
""")

# REGISTER
async def register_user(user_id, username, name):
    cursor.execute(f'INSERT INTO users VALUES(?, ?, ?, ?);', (user_id, username, name, "Бронза"))
    connect.commit()

# UPDATE

# SELECT
async def select_status_user(user_id):
    result = cursor.execute(f'SELECT status FROM users WHERE user_id = {user_id}').fetchone()
    result = result[0]
    connect.commit()

    return result

async def select_status_register_user(user_id):
    cursor.execute(f'SELECT user_id FROM users WHERE user_id = {user_id}')
    if cursor.fetchone() is None:
        result = 'No'
    else:
        result = 'Yes'

    return result

async def select_cods():
    result = cursor.execute('SELECT cod FROM cods').fetchall()
    connect.commit()

    return result

# DELETE