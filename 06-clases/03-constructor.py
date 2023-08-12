print("\n==========  constructor  ====================\n")

# self   acce la referencia de atributo ó metodos

class Carrera:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    # acceder propiedad de atributos __init__()
    def materias(self):
        print(f"{self.nombre} {self.apellido} se registro en EStructura de Datos I")

#obj1 = Carrera("Base de Datos I")
#print(obj1.nombre)

obj2 = Carrera("Jimena", "Claros Rivera", None)
obj2.materias()


