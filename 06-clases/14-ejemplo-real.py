#print("\n==========  ejercicio de herencia  ====================\n")

class Model():
    tabla = False
    
    def __init__(self):
        if not self.tabla:          # sí no esta definida la tabla
            print("Error, tienes que definir una tabla")

    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")
        
    @classmethod   # decorador
    def buscar_por_id(self, _id):   # _id  es variable activa de python
        print(f"Buscando por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"
    
obj = Usuario()
#obj.guardar()
obj.buscar_por_id(145)
