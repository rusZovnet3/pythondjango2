print("\n========================  kwargs  =================================")
# muestra como archivo Json  ó diccionario

def get_product(**datos):
    #print(datos)
    print(datos["nom"], datos["edad"])   # mostrar el dato especifico
    
get_product(id="id", nom="Lurdes", ape="Calderon", edad=29)