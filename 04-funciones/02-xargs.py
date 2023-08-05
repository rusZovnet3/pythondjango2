print("\n========================  Xargs  =================================")

def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

suma(2, 5)
suma(3, 4, 3, 6)
suma(8)
suma(5, 0, 15)
suma(12, 18)
