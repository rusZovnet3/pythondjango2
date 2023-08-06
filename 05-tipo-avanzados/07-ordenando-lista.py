print("\n==========  ordenando - lista  ====================\n")

numeros = [15, 2, 3.45, 14, 22, 7, 5, 8, 5, 6, 7, 5, 11]

usuarios = [
    [4, "Anahi"], 
    [2, "Lurdes"], 
    [5, "Blanca"], 
    [1, "Maria Vctoria"], 
    [3, "Eliana"]
    ]

usuarios1 = [
    ["Gabriela Ines", 4], 
    ["Liliana", 3], 
    ["Yenny Rossana", 1], 
    ["Rosio", 5], 
    ["Yanine", 2]
    ]

print("\n\t\t\t---------  sort()  ---------------n")

# ordenar de forma ascedentes

""" numeros.sort()
print(numeros) """

# ordenar de forma descendentes

""" numeros.sort(reverse=True)
print(numeros) """

print("\n\t\t\t---------  sorted()  ---------------n")

# ordenar de forma ascendentes, en una nueva lista

""" num2 =sorted(numeros)
print(numeros)
print(num2) """


# ordenar de forma descendentes, en una nueva lista

""" num2 =sorted(numeros, reverse=True)
print(numeros)
print(num2) """


""" usuarios.sort()
print(usuarios) """

#-------------
# ordenar de forma ascendentes, en una nueva lista


""" def ordena(elem):
    return elem[1] """

""" usuarios1.sort(key=ordena)
print(usuarios1) """


# ordenar de forma descendentes, en una nueva lista

""" usuarios1.sort(key=ordena, reverse=True)
print(usuarios1) """

print("\n\t\t\t--------- expresiones lambda()  ---------------n")

# descendente
#usuarios1.sort(key=lambda el: el[1], reverse=True)
usuarios1.sort(key=lambda el: el[1])
print(usuarios1)
