print("\n==========  Metodos Magicos  ====================\n")

class Carrera:

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    # metodo magic  __del__      destructor ----------
    def __del__(self):
        print(f"Formateo completo {self.nombre}")
        
    # metodo magic __str__  -----------------
    def __str__(self):
        return f"Clase Carrera: {self.nombre}"

    def materias(self):
        print(f"{self.nombre}: Me registre en Redes 1")


obj1 = Carrera("Maria Victoria", "Orellana Meyui", 30)
""" print(obj1)


texto = str(obj1)
print(texto) """

del obj1


# metodos magicos  : magic methods python
# https://rszalski.github.io/magicmethods
