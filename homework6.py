import sqlite3
datab = sqlite3.connect('game.datab')
c = datab.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS game(
name TEXT,
age INTEGER,
password INTEGER

)''')
c.execute('''INSERT INTO game VALUES('nurs',18,886723)''')

datab.commit()
datab.close()