from pathlib import Path
from zipfile import ZipFile



# comprime desde la carpeta Curso02 tdos sus archivos y carpetas dentro del directorio Curso02
# with ZipFile("archivos/comprimidos.zip", "w") as zip:
#     # Curso02
#     # rglob("*.*")   = (cualquier nombre, cualquier eztension), incluye tambien a las carpetas
#     for path in Path().rglob("*.*"):
#         print(path)
#         if str(path) != "archivos/comprimidos.zip":   # verifica que no se comprima al archivo creado
#             zip.write(path)


# Leer

with ZipFile("archivos/comprimidos.zip") as zipp:
    #print(zip.namelist())       # listado de rutas de archivos
    
    # buscar el archivo dentro del zip
    # info = zipp.getinfo("archivos/06-comprimidos.py")        
    # print(
    #     info.file_size,
    #     info.compress_size
    # )
    # extraer archivos del zip
    zipp.extractall("archivos/descomprimidos")


