import sqlite3

conn = sqlite3.connect("data.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, text TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY, text TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, text TEXT)")

def insert_data(table, text):
    cursor.execute(f"INSERT INTO {table} (text) VALUES (?)", (text,))
    conn.commit()

def get_all(table):
    cursor.execute(f"SELECT * FROM {table}")
    return cursor.fetchall()

def delete_item(table, item_id):
    cursor.execute(f"DELETE FROM {table} WHERE id=?", (item_id,))
    conn.commit()

def update_item(table, item_id, new_text):
    cursor.execute(f"UPDATE {table} SET text=? WHERE id=?", (new_text, item_id))
    conn.commit()

def delete_all(table):
    cursor.execute(f"DELETE FROM {table}")
    conn.commit()