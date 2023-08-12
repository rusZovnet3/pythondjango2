print("\n==========  metodos de clases  ====================\n")

class Carrera:
    credito = 5
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # Factory method
    @classmethod
    def materias(cls):
        print("Estructura de Datos I")

    @classmethod
    def fabrica(cls):
        # es lo mismo  cls ==> Carrera  la clase
        return cls("Rosmery", "Condori Toledo", 31)

Carrera.materias()

obj1 = Carrera("Carla", "Vaca Suarez", 32)
obj2 = Carrera("Marisol", "Gonzales Hinojosa", 27)

obj3 = Carrera.fabrica()
print(obj3.edad, obj3.nombre)


