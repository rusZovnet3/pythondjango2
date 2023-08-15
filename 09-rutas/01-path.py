#  libreria de path
from pathlib import Path

print("\n---------------------  Path ó rutas  ---------------------\n")

# r   formateo de backlabs \

""" # windows
Path(r"C:\Program Files\Adobe")

# linux
Path("usr/bin")   # ruta absoluta

Path()   # nos muestra la ruta de la carpeta

Path.home()

Path("one/__init__.py")   # ruta relativa """

path = Path("hola-mundo/mi-archivo.py")

path.is_file()          # para saber sí es un archivo
path.is_dir()           # para saber sí es un directorio ó carpeta
path.exists()           # sí existe

print(
    path.name,          # nombre del archivo incluido la extension
    path.stem,          # nombre del archivo
    path.suffix,        # la extension   ej: .py
    path.parent,        # carpeta padre del archivo
    path.absolute()     # la ruta completa del archivo
)

# with_name   permite renombrar el nombre del archivo y tambien su extension
p = path.with_name("hola-python.exe")

# with_suffix   permite cambiar la extension
q = p.with_suffix(".json")

# with_stem    permite cambiar el nombre del archivo, no la extension
r = q.with_stem("programacion")


print(p)
print(q)
print(r)
