import sqlite3

with sqlite3.connect("11-sqlite/app.db") as con:
    cursor = con.cursor()
    # datos sqlite
    usuarios = [
        (2, "Python y Django"), (3, "Html5 y Css3"), (4, "AK47"), (5, "Rosmery Condori"), (6, "Rosio Pedraza")
    ]
    # ejecuta multiples datos
    cursor.executemany(
        "insert into usuarios values(?, ?)",
        usuarios,
    )