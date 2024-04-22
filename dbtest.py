import sqlite3

username = "qw32e"
password = "11"
con = sqlite3.connect("films_db.sqlite")
cur = con.cursor()

result = cur.execute("""SELECT * FROM Films
                        WHERE  username = ? AND password = ?""", (username, password)).fetchall()

print(result)

if not result:
    print("regok")
    cur.execute("""INSERT INTO Films(username, password) VALUES (?,?)""", (username, password))
    con.commit()

print(cur.execute("SELECT * FROM Films").fetchall())