print("\n==========  Anulación de Metodos  ====================\n")

class DeviceElectronic:
    
    def hardware(self):
        print("Material de Aluminio y vidrio")
        
    def software(self):
        print("gestores de aplicasiones")
        
    def firmware(self):
        print("Sistema Operativo")
        
class ComponentesExterno:
    
    def __init__(self):
        self.aqui = "segunda clase"
    
    def device(self):
        print("Impresoras")
        
    def network(self):
        print("Conexion Inalambrica")
        
    def fabricacion(self):
        print("ensamblaje en Argentina")
        
class ComponenteIntegrado(ComponentesExterno):
    
    def __init__(self):
        super().__init__()    # invocando el constructor de la segunda clase
        self.nada = "tercera clase"
    
    def componentes(self):
        print("micro condensadores")
        
    def fabricacion(self):
        print("Hecho en China")
        #super().fabricacion()   # metodo de acceso a las funciones de la clase
        
        
obj1 = ComponenteIntegrado()    # clase 3
obj1.fabricacion()              # clase3

print(obj1.aqui, obj1.nada)     # clase3
        
        
        