import sqlite3

con = sqlite3.connect("11-sqlite/app.db")
# creacion de consultas
cursor = con.cursor()           
# creacion del metodo
cursor.execute(
    """
    CREATE TABLE if not exists usuarios
    (id INTEGER primary key, nombre VARCHAR(50));
    """
)
# graba los cambios, y ejecuta
con.commit()
con.close()



