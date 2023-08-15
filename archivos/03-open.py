from io import open


# lectura     read   =  'r'
# escritura   write  =  'w'
# agregar



# Escritura

""" texto = "Hola evelin"

archivo = open("archivos/hola-evelin.txt", "w")     # abrir archivo

# sí no existe el archivo, se crea automaticamente
archivo.write(texto)                                # escribiendo el archivo
archivo.close()                                     # cerrar el archivo """


# Lectura
""" archivo = open("archivos/hola-evelin.txt", "r")
texto = archivo.read()
archivo.close()

print(texto) """


#Lectura como Lista, cada linea del texto, lo separa como elemento de la lista

""" archivo = open("archivos/hola-evelin.txt", "r")
texto = archivo.readlines()
archivo.close()

print(texto) """


# with  y seek
""" with open("archivos/hola-evelin.txt", "r") as archivo:
    print(archivo.readlines())      # multiples lineas
    archivo.seek(0)  # permite verificar por caracter, y no linea
    for linea in archivo:    # lista
        print(linea) """
        
        

# agregar        
        
""" archivo = open("archivos/hola-evelin.txt", "a+")
archivo.write("aumentando un elemento")
archivo.close()    """     
 
 
 
# Lectura y Escritura

with open("archivos/hola-evelin.txt", "r+") as archivo:
# leer todas las lineas que existen y devuelve en Lista
    texto = archivo.readlines()                 
    archivo.seek(0)                      # permiteverificar por caracter
    texto[0] = "practicando python de basico a intermedio"  # cambiar la primera linea el texto
    print(texto)
    archivo.writelines(texto)       # escribir el texto dentro el archivo
   
        