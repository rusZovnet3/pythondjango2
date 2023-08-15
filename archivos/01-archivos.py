from pathlib import Path
from time import ctime


archivo = Path("archivos/archivos-prueba.txt")

# archivo.exists()            # sí existe el archivo
# archivo.rename()            # renombrar el archivo
# archivo.unlink()            # para eliminar el archivo


#print(archivo.stat())          # para mostrar la estadistica del archivo

""" st_size                     # Tamaño del archivo
st_atime                    # fecha de acceso
st_mtime                    # fecha de modificacion
st_ctime                    # fecha de creacion (windows), cambio de metadadtos (linux, macox) """


#print("acceso", archivo.stat().st_atime)               # datos de timestamp, (Unix)

print("acceso", ctime(archivo.stat().st_atime))         # datos en fecha legible
print("creación", ctime(archivo.stat().st_ctime))
print("modificación", ctime(archivo.stat().st_mtime))






