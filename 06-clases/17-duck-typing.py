print("\n==========  Duck Typing  ====================\n")


class Usuario():
    
    def guardar(self):
        print("Guardando en DataBase")
        
        
class Sesion():

    def guardar(self):
        print("Guardando en Archivo")
        
        
def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()
 
        
usuario = Usuario()
sesion = Sesion()

guardar([sesion, usuario])   
