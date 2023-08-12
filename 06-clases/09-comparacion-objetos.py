print("\n==========  Comparación de Objetos  ====================\n")

class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        
    # metodo magic __eq__  que sirve para comparar objetos
    def __eq__(self, otro):
        return self.lat == otro.lat and self.lon == otro.lon
    
    
    # metodo magic __ne__  (no es igual) que sirve para comparar negando el objeto
    def __ne__(self, otro):
        return self.lat != otro.lat or self.lon != otro.lon
    
    # metodo magic  __lt__  menor igual
    def __lt__(self, otro):
        return self.lat + self.lon < otro.lat + otro.lon
    
    
    # menor igual que
    def __le__(self, otro):
        return self.lat + self.lon <= otro.lat + otro.lon
        

coords1 = Coordenadas(45, 27)
coords2 = Coordenadas(45, 27)
coords3 = Coordenadas(44, 27)

"""# invoca metodo __eq__
print(coords1 == coords2)   # True

"""


""" # invoca metodo __ne__
print(coords1 != coords2)   # False """


""" # invoca metodo __lt__
print(coords3 < coords2)   # True
print(coords3 > coords2)   # False
 """

# invoca metodo __le__
print(coords3 <= coords2)   # True
print(coords3 >= coords2)   # False

print(coords1 >= coords2)   # True