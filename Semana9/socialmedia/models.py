import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath((__file__)))

def create_post(name, content):
    connection = sql.connect(path.join(ROOT, 'database.db'))
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS posts(id INTEGER PRIMARY KEY AUTOINCREMENT,\
                    name TEXT NOT NULL, content TEXT NOT NULL)')
    cursor.execute('INSERT INTO posts(name, content) VALUES(?, ?)', (name, content))
    connection.commit()
    connection.close()
    
def get_posts():
    connection = sql.connect(path.join(ROOT, 'database.db'))
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS posts(id INTEGER PRIMARY KEY AUTOINCREMENT,\
                    name TEXT NOT NULL, content TEXT NOT NULL)')
    cursor.execute('SELECT * FROM posts')
    return reversed(cursor.fetchall())

