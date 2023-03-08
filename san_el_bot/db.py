import sqlite3
import time
import json

connect = sqlite3.connect("database.db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id INT PRIMARY KEY,
    username TEXT,
    name TEXT,
    status TEXT,
    cart_santeh TEXT DEFAULT None,
    cart_elek TEXT DEFAULT None,
    phone_nomber TEXT DEFAULT None,
    delivery_unloading TEXT DEFAULT None,
    comment TEXT DEFAULT None
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS cods(
    cod TEXT
)
""")

# REGISTER
async def register_user(user_id, username, name):
    cursor.execute('INSERT INTO users VALUES(?, ?, ?, ?)', (user_id, username, name, "Бронза"))
    connect.commit()


# UPDATE
async def add_cart_santeh(user_id, cart: dict):
    cursor.execute('UPDATE users SET cart_santeh = ? WHERE user_id = ?', (json.dumps(cart), user_id))
    connect.commit()

async def add_cart_elek(user_id, cart: dict):
    cursor.execute('UPDATE users SET cart_elek = ? WHERE user_id = ?', (json.dumps(cart), user_id))
    connect.commit()

async def add_phone_nomber(user_id, phone_nomber):
    cursor.execute('UPDATE users SET phone_nomber = ? WHERE user_id = ?', (phone_nomber, user_id))
    connect.commit()

async def add_delivery_unloading(user_id, delivery_unloading):
    cursor.execute('UPDATE users SET delivery_unloading = ? WHERE user_id = ?', (delivery_unloading, user_id))
    connect.commit()

async def add_comment(user_id, comment):
    cursor.execute('UPDATE users SET comment = ? WHERE user_id = ?', (comment, user_id))
    connect.commit()


# SELECT
async def select_name(user_id):
    result = cursor.execute(f'SELECT name FROM users WHERE user_id = {user_id}').fetchone()
    result = str(result[0])
    connect.commit()
    
    return result

async def select_cart_santeh(user_id):
    result = cursor.execute(f'SELECT cart_santeh FROM users WHERE user_id = {user_id}').fetchone()
    result = json.loads(result[0])
    connect.commit()

    return result

async def select_cart_elek(user_id):
    result = cursor.execute(f'SELECT cart_elek FROM users WHERE user_id = {user_id}').fetchone()
    result = json.loads(result[0])
    connect.commit()

    return result

async def select_phone_nomber(user_id):
    result = cursor.execute(f'SELECT phone_nomber FROM users WHERE user_id = {user_id}').fetchone()
    result = str(result[0])
    connect.commit()

    return result

async def select_delivery_unloading(user_id):
    result = cursor.execute(f'SELECT delivery_unloading FROM users WHERE user_id = {user_id}').fetchone()
    result = str(result[0])
    connect.commit()
    
    return result

async def select_comment(user_id):
    result = cursor.execute(f'SELECT comment FROM users WHERE user_id = {user_id}').fetchone()
    result = str(result[0])
    connect.commit()
    
    return result

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