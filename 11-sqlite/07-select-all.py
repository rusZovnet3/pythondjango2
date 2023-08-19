import sqlite3

# fetchall()   muestra todos los registro de la tabla
# muestra en una lista, con multiples Tuplas

with sqlite3.connect("11-sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute("SELECT * FROM usuarios")
    print(cursor.fetchall())