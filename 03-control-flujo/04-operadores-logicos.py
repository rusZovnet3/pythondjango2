print("=============  and, or, not --- operador logico =============\n")

edad = input("Ingrese su edad: ")
edad = int(edad)
licencia = input("Escriba su nro de Licencia: ")
licencia = int(licencia)
#licencia = int(licencia)
gas = True
encendido = True

if edad >= 18 and edad <= 60:
    if not gas:
        print("No puedes manejar")
    elif licencia or encendido:
        print("Puedes manejar")
else:
    print("No esta autorizado manejar, por menor de edad")
        