import sqlite3 as sq


with sq.connect('saper_2.db') as con:
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS users (
        name TEXT,
        sex INTEGER,
        old INTEGER,
        score INTEGER
    )''')

    cur.execute("SELECT * FROM users WHERE score > 100 ORDER BY score DESC LIMIT 5")
    for result in cur:
        print(result)
