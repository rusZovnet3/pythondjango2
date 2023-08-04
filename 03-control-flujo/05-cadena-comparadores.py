print("=============   =============\n")

# Mostrar la edad de acceso al cuartel
edad = input("Escriba su Edad: ")
edad = int(edad)


#if edad >= 18 and edad <= 25:
if 18 <= edad <= 25:
    print("Esta autorizado para entrar al cuartel")
else:
    if edad < 18:
        print("Eres menor de edad")
    elif edad > 25:
        print("Eres muy viejo para entrar")
    
