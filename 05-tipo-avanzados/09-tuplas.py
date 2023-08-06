print("\n==========  Tuplas  ====================\n")

numeros = (3, 5, 6) + (2, 1, 4)
print(numeros)

print("\n\t\t\t---------------  tuple()  --------------\n")

punto = tuple([1, 2])
print(punto)    # resultado de una tupla


menosNum = numeros[:2]
print(menosNum)

print("\n\t\t\t---------------  Desenpaquetar  --------------\n")

# Desenpaquetar
primero, segundo, *otros = numeros
print(primero, segundo, otros)  # devuelve en una lista

print("\n\t\t\t---------------  Iterar  --------------\n")

for n in numeros:
    print(n)

print("\n\t\t\t---------------  Modificar  --------------\n")
# no se puede cambiar datos de la tupla
# sí se puede cambiar elemento de la lista

listaNumeros = list(numeros)    # crear una lista en base de la Tupla
listaNumeros[1] = "Html"   # cambiar elemento de la lista
print(listaNumeros)

