print("\n==========  Operador Desempaquetador  ====================\n")

miLista1 = [4, 1, 5, 3, 2]   # lista
miLista2 = (4, 1, 5, 3, 2)  # Tupla
#print(miLista1)

#print(*miLista1)  # valores
print(*miLista2)    # valores

print("\n\t\t------------------------------\n")

miLista3 = [14, 8]

""" combinada = [*miLista1, *miLista3]
print(combinada) """

combinada1 = [15.7, *miLista1, "Practica", True, *miLista3]
print(combinada1)


print("\n\t\t-------------- diccionarios ----------------\n")

punto1 = {"x": 25}
punto2 = {"y": 14}

npunto = {**punto1, **punto2}
print(npunto)

print("\n\t\t------------------------------\n")

punto3 = {"x": 25, "y": "Hola"}
punto4 = {"y": 14}

#npunto1 = {**punto3, **punto4}
#print(npunto1)

npunt2 = {**punto3, "tiempo": 15, **punto4, "z": "Python"}
print(npunt2)