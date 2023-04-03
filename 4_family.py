import sqlite3 as sq


with sq.connect('family.db') as con:
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS family (
        name TEXT,
        sex INTEGER,
        old INTEGER


    )''')
