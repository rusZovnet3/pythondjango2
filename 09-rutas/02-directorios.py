from pathlib import Path

print("\n==========  Directorios  ====================\n")

path = Path("09-rutas")

# path.exists()               # existe el directorio
# path.mkdir()                # crear el directorio
# path.rmdir()                # cuando está vacio, se elimina la carpeta
# path.rename()               # cambiar el nombre del directorio

print("\n\t\t\t-------Mostrar la rutas del directorio actual-----------------\n")
# ver las rutas del directorio
for px in path.iterdir():
    print(px)


# PosixPath   ==>  linux, MacOx
# WindowsPath ==>  Windows

# ver la ruta en una lista
print("\n\t\t\t---------Mostrar la ruta de cada archivo en la lista------------\n")

archivo1 = [p for p in path.iterdir() if not p.is_dir()]
print(archivo1)

print("\n\t\t\t------------Mostrar los archivos con extension de Python-------------\n")

archivo2 = [p for p in path.glob("*.py")]
print(archivo2)

print("\n\t\t\t-------------- Mostrar archivo de python con nombre inicial '01-' ------\n")

archivo3 = [p for p in path.glob("01-*.py")]
print(archivo3)


# busca del directorio actual hasta el subdirectorio del los archivos
print("\n\t\t\t-- Mostrar archivo de python, que se encuentren en todas las carpetas' ------\n")

archivo4 = [p for p in path.glob("**/*.py")]
print(archivo4)


print("\n\t\t\t----- Mostrar archivo de python, que se encuentren en todas las carpetas ----\n")
# otro metodo

archivo5 = [p for p in path.rglob("*.py")]
print(archivo5)