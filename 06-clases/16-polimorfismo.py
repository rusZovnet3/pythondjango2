from abc import ABC, abstractmethod

print("\n==========  Polimorfismo  ====================\n")

class Model(ABC):
    
    @abstractmethod
    def guardar(self):
        pass

class Usuario(Model):
    
    def guardar(self):
        print("Guardando en DataBase")
        
        
class Sesion(Model):

    def guardar(self):
        print("Guardando en Archivo")
        
        
def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()
        
        
""" usuario = Usuario()
guardar(usuario)    """     
        
usuario = Usuario()
sesion = Sesion()

guardar([sesion, usuario])   

  