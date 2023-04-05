import sqlite3 as sq


with sq.connect('union.db') as con:
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS tab1(
        score INTEGER,
        `from` TEXT
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS tab2 (
        val INTEGER,
        `type` TEXT
    )''')
