from abc import ABC, abstractmethod

# abc  == abstract class, nombre de la clase
#print("\n==========  Clases Abstractas  ====================\n")

class Model(ABC):
    
    """ def __init__(self):
        if not self.tabla:          # sí no esta definida la tabla
            print("Error, tienes que definir una tabla") """
       
    @property
    @abstractmethod     
    def tabla(self):
        pass

    @abstractmethod
    def guardar(self):
        pass
        
    @classmethod   # decorador
    def buscar_por_id(self, _id):   # _id  es variable activa de python
        print(f"Buscando por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"
    
    def guardar(self):
        print("Guardando Usuario..")
    
#  no puede ser objeto, la clase abstracta
#model = Model()
#model.buscar_por_id(145)

usuario = Usuario()
usuario.guardar()
usuario.buscar_por_id(3221994)

