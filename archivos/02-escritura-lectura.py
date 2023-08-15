from pathlib import Path

archivo = Path("archivos/archivos-prueba.txt")
#texto = archivo.read_text()                        # 1 linea
#texto = archivo.read_text().split("\n")            # multiple linea

texto = archivo.read_text("utf-8").split("\n")      # para visualizar, read_text()  -- codificacion de texto
#print(texto)


texto.insert(1, "Hola Viky")                        # para insertar el texto y la posicion de linea
# write_text : escribir al archivo, "\n" salto de linea, join() escribir el texto en esa posicion, con codificacion
archivo.write_text("\n".join(texto), "utf-8")       # para guardar el texto y la codificacion


# write_text : escribir al archivo,  "reemplaza al texto del archivo" con la codificasion
#archivo.write_text("Hola Python", "utf-8")


