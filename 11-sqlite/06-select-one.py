import sqlite3

# fetchone()   muestra el primer registro de la tabla

with sqlite3.connect("11-sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute("SELECT * FROM usuarios")
    print(cursor.fetchone())