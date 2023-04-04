import sqlite3 as sq

with sq.connect('saper_6.db') as con:
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS users(
        name TEXT,
        sex INTEGER,
        old INTEGER,
        score INTEGER
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS games(
        user_id INTEGER,
        score INTEGER,
        time INTEGER

    )''')
