import json
from pathlib import Path

# escribir json

# productos = [
#     {"id": 1, "name": "Memoria RAM"},
#     {"id": 2, "name": "Disco Duro"},
#     {"id": 3, "name": "Disquetera"},
#     {"id": 4, "name": "Pendrive"}
# ]

# Mostrar en una lista los diccionario
#data = json.dumps(productos)
#print(data)

# crear el archivo json con sus datos (listado de diccionarios)
#Path("archivos/productos.json").write_text(data)


#  leer json
data = Path("archivos/productos.json").read_text(encoding="utf-8")
productos = json.loads(data)
#print(productos)


# Modificar json   -  json.dumps(productos)  transforma en json
productos[0]["name"] = "Realizando cambios"
Path("archivos/productos.json").write_text(json.dumps(productos))

