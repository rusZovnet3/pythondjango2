print("\n========================  Listas =================================\n")


dato = [45, ["Hola", 12, "Lurdes", [78, "30", False], ["Bolivia", False, [False, 4500, [1, 5, "Hola"], "Andrade"], 15.4], 58], "Feliz", [14, True], 0, [3.99, [100, "Calderon", True], "años"], " "]

pal = ["python", "diseño web", True, 16.45, "localhost", 1500, "Viky", "Sapee"]

#print(dato[1][0] + dato[6] + dato[1][2] + dato[6] + dato[5][1][1] + dato[6] + dato[1][4][2][3])

# cambiar dato de la lsta

dato[0] = "Jessica"
#print(dato)

# mostrar los 3 elementos
#print(dato[0:3])
#print(dato[:3])

# mostrar los ultimos tres elementos
#print(dato[2:])

""" print(pal[2:])   # posicion 2 hasta la posicion hasta el final
print(pal[:4])   # posicion 0,  empieza contar del 0 como numero 1 hasta el 4
print(pal[-3])   # cuenta de lado izquierdo, osea la posicion final empieza ser -1 de la lista
print(pal[::2])  # muestra los datos en posicion inicial 0 en 2 saltos
print(pal[1::2]) # muestra los datos en posicion inicial 1 en 2 saltos """

numer = list(range(1, 21))
print(numer[::2])       # mostrar los numeros inpares
print(numer[1::2])      # mostrar los numeros pares

