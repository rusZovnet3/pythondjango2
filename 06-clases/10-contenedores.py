print("\n==========  Contenedores  ====================\n")

#

class Producto:
    def __init__(self, nombre, precio):    
        self.nombre = nombre
        self.precio = precio
        
    def __str__(self):
        return f"Producto: {self.nombre} - Precio: {self.precio}"
        

class Categoria:
    productos = []      # lista
    
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos
    
    # agregar más productos
    def agregar(self, producto):
        self.productos.append(producto)    # agregar los elemento a la lista producto
        
    def imprimir(self):
        for producto in self.productos:    # desglosa la lista de productos
            print(producto)
            
            
beisbol = Producto("Beisbol", 45)
bicicleta = Producto("Bicicleta", 150)
raqueta = Producto("Raqueta", 100)
baloncesto = Producto("Baloncesto", 85)

#print(beisbol)

deporte = Categoria("Deporte", [beisbol, raqueta])
deporte.agregar(baloncesto)
deporte.agregar(bicicleta)

deporte.imprimir()


