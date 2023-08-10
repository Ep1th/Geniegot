import csv, sqlite3




con = sqlite3.connect('SQLDB.db')
cur = con.cursor()
cur.execute("""CREATE TABLE info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nature TEXT,
            bookofwise TEXT
)""")

with open('testt.csv', 'r', encoding="utf8") as f:
    dr = csv.DictReader(f, delimiter="[")
    to_db = [(i['Натура'], i['СтрокаИзКнигиМудрости']) for i in dr]

cur.executemany("INSERT INTO info (nature, bookofwise) VALUES (?, ?);", to_db)
con.commit()
con.close()
