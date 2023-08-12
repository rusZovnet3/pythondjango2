print("\n==========  Propiedades de clases  ====================\n")

class Carrera:
    credito = 5
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    # acceder propiedad de atributos __init__()
    def materias(self):
        print(f"{self.nombre} {self.apellido} se registro en EStructura de Datos I")


""" obj1 = Carrera("Jimena", "Claros Rivera", None)
print(Carrera.credito) """

Carrera.credito = 10

# * el cambio del dato del atributo de la clase
#   se cambiará el dato del atributo de la clase

# * sí es cambiado el atributo su valor de la clase en un objeto
#   se cambiará solo para el objeto 

obj2 = Carrera("Marisol", "Gonzales Hinojosa", 27)
obj2.credito = 8
 

obj3 = Carrera("Celia", "Garcia Mendez", 28)

print(Carrera.credito)
print(obj2.credito)
print(obj3.credito)