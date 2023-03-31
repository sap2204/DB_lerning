import sqlite3 as sq

with sq.connect('cars.db') as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS cars (
        marka TEXT,
        name TEXT,
        price INTEGER
    )""")
    
