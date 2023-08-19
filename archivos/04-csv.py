import csv
import os

# escribir

# with open("archivos/archivo.csv", "w") as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow(["twit_id", "user_id", "text"])
#     writer.writerow([1000, 1, "escribiendo codigo python"])
#     writer.writerow([1001, 2, "escribiendo codigo javascript"]) 

### error : como resultado, crea linea de espacio,  eliminar linea de espacio de csv?


# Leer

with open("archivos/archivo.csv") as archivo:
    reader = csv.reader(archivo)
    #print(reader)
    print(list(reader))
    archivo.seek(0)             
    for linea in reader:        # mostrando linea por linea
        print(linea)


# Actualizar csv, actualizar el dato

# todos los datos se transforman en string,
# del csv, ya sea entero, float etc.

            # archivo oficial modo lectura     archivo temporal en modo escritura
""" with open("archivos/archivo.csv") as r, open("archivos/archivo_temp.csv", "w") as w:
    reader = csv.reader(r)          # archivo actual con el metodo leer
    writer = csv.writer(w)          # archivo temporal con el metodo escritura
    for linea in reader:
        if linea[0] == "1000":
            writer.writerow([1000,1,"Texto Modificado nuevamente"])   # modificar la linea
        else:
            writer.writerow(linea)                     # mantener el archivo       
os.remove("archivos/archivo.csv")
os.rename("archivos/archivo_temp.csv", "archivos/archivo.csv") """
