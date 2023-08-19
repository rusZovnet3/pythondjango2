import sqlite3

# with por defecto, al final ya tiene la sintaxis de ejecutar y cerrar la db
# commit()   y  close()

with sqlite3.connect("11-sqlite/app.db") as con:
    cursor = con.cursor()           
    cursor.execute(
        """
        CREATE TABLE if not exists usuarios
        (id INTEGER primary key, nombre VARCHAR(50));
        """
    )