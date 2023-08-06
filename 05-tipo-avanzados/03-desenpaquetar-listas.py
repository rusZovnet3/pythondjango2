print("\n==========  Desempaquetar Listas  ====================\n")

numeros = [11, 25, 14, 5, 1400, 0.665]

""" primero, segundo, tercero, cuarto = numeros
print(primero, segundo, tercero, cuarto) """

#primero, segundo, *otros = numeros
#print(primero, segundo, otros)

num = list(range(1, 10))

# *variable   --> muestra la lista agrupada de elemntos
# crea nuevas posiciones en la lista
""" primero, *otros, ultimo = num
print(primero, otros, ultimo) """


# desglosa por variable igualando a la variable lista
primero, segundo, *otros, penul, ultimo = num
print(segundo, ultimo, otros, penul)