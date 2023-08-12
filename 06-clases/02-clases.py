print("\n==========  clases  ====================\n")

class Carrera:
    def materias(self):
        print("EStructura de Datos I")
        
area = Carrera()
#print(type(area))
var1 = 55

area.materias()

# isinstance(este obj es instancia, de la clase)
print(isinstance(area, Carrera))    #  es su instancia
print(isinstance(var1, Carrera))  # no es su instancia
