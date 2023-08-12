print("\n==========  Propiedades y métodos privados  ====================\n")

# para renombrar variable unico y que se renombre automatico con Vcode
# shit + ctrl + P
# rename symbol

class Carrera:

    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre     # atributo privado
        self.apellido = apellido
        self.edad = edad
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre1):
        self.__nombre = nombre1
    
    def materias(self):
        print(f"{self.__nombre}: Me registre en Redes 1")
        
    @classmethod    
    def fabrica(cls):
        # es lo mismo  cls ==> Carrera  la clase
        return cls("Rosmery", "Condori Toledo", 31)

obj1 = Carrera.fabrica()    # ya tiene el dato como objeto, es donde extrae el nombre
obj1.materias()             # muestra en el metodo

# no se puede mostrar el atributo 'privado' fuera de la clase, ni modificar
#print(obj1.__nombre)          


# se puede mostrar el atributo privado, siempre que este dentro de un metodo de la clase
# no se podra modificar
#print(obj1.get_nombre())


# muestra en Diccionario con los elementos
# a los atributos privados muestra como elemento  _nombreClase__atributo

#print(obj1.__dict__)


# muestra el valor del elemento privado
print(obj1._Carrera__nombre)
