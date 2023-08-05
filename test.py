import csv, sqlite3




con = sqlite3.connect('cogs/SQLDB.db')
cur = con.cursor()
cur.execute("""CREATE TABLE jokes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            content TEXT
)""")

with open('testt.csv', 'r', encoding="utf8") as f:
    dr = csv.DictReader(f, delimiter="[")
    to_db = [(i['name'], i['content']) for i in dr]

cur.executemany("INSERT INTO jokes (name, content) VALUES (?, ?);", to_db)
con.commit()
con.close()
