print("\n==========  Decorador property  ====================\n")

class Carrera:

    def __init__(self, nombre):
        #self.nombre = nombre
        self.nombre = nombre
        
    @property    # estaran oculto
    def nombre(self):
        print("Pasando por getter")
        return self.__nombre
    

    @nombre.setter    # estaran oculto, se indicara que es metodo setter
    def nombre(self, nombre):
        print("pasando por setter")
        if nombre.strip():
            self.__nombre = nombre
        return
    
    

#obj1 = Carrera("Sistemas para el Soporte para la toma de Desiciones")

# muestra el uso de memoria
#print(obj1)

obj2 = Carrera("Sistemas para el Soporte para la toma de Desiciones")
""" print(obj2.get_nombre()) """

print(obj2.nombre)
