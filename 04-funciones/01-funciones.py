print("\n========================  Funciones  =================================")

print("\t\t\t--------- Simples ---------------\t")

def funcionA():
    print("Python")
    
#funcionA()

print("\n\t\t\t--------- Parametros y Argumentos ---------------\t")
def nombreC():
    return input("Ingrese su nombre: ")

def apellidoC():
    return input("Ingrese su apellido: ")


def funcionB(dato):     # parametros
    print(f"Bienvenidos {dato}")
    
def funcionC(nom, ape):  # argumentos
    print(f"Felicitaciones {nom} {ape} ....")
    
#funcionB(nombreC())         # parametros
#funcionB("Maria Victoria")  # argumnetos

#funcionC(nombreC(), apellidoC())


print("\n\t\t\t--------- Parametros Opcionales ---------------\t")

def funcionD(nom, edad = 30):
    print(f"Me llamo {nom} y tengo {edad} años")
    
#funcionD(nombreC(), 25) 
#funcionD(nombreC())


print("\n\t\t\t--------- Argumentos Nombrados ---------------\t")
# indicar el parametro especifica creado a la funcion

funcionC(ape="Gonzales Hinojosa" ,nom="Marisol")