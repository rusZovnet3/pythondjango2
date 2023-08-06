print("\n==========  sets  ====================\n")
# set significa grupo ó conjunto

val1 = {1, 4, 5, 10, 2, 4, 9, 3, 7, 2, 6}
val2 = [3, 5, 7, 2, 1, 8, 11]

#  remueve los valores repetidos y los ordena en ascendentes
#print(val1)

""" val1.add(10)    # agrega al ultimo elemento
val1.remove(2)
print(val1) """

# convertir de lista a set
val2 = set(val2)
#print(val2)

print(val1)
print(val2)

print("\n\t\t\t------------  operador union --  !  -------------\n")

# unifica los set val1 y set val2, sin repeticion de elemento
#  !  significa  union
print(val1 | val2)

print("\n\t\t\t------------  operador interseccion --  &  -------------\n")

# interseccion ,  muestra los elemento que se encuentra repetido en ambas set()
# &  operador interseccion
print(val1 & val2)


print("\n\t\t\t------------  operador diferencia --  -  -------------\n")
# comparar del conjunto val1  eliminando los elementos que existe en el conjunto val2
# como resultado se mostrara el conjunto val1

print(val1 - val2)

print("\n\t\t\t------------  operador simetrica --  ^  -------------\n")
# muestra los elementos que no se encuentran en ambos conjunto,
# de forma ordenada ascendentes

print(val1 ^ val2)


#  los set() no se puede identificar la indice del elemento especifico del conjunto

# para identificar si existe el elemnto
if 5 in val2:
    print("Existe")

