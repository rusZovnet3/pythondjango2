print("\n========================  alcances  =================================")
# variable global
mensaje = 30

def funcionA():
    mensaje = "Hola Python"
    print(mensaje)
    
def funcionB():
    mensaje = 55
    print(mensaje)
    
def funcionC():
    mensaje = "Developer Design"
    print(mensaje)
    
def funcionD():
    global mensaje
    mensaje = "Hola Wendy"
    print(mensaje)
    
#print(mensaje)
#funcionC()

#print(mensaje)
#funcionD()
#print(mensaje)

resultado1 = mensaje + 3
print(resultado1)
funcionD()
resultado2 = mensaje + 3
print(resultado2)
