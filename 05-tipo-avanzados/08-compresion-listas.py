print("\n==========  Compresion Listas  ====================\n")


usuarios = [
    ["Gabriela Ines", 4], 
    ["Liliana", 3], 
    ["Yenny Rossana", 1], 
    ["Rosio", 5], 
    ["Yanine", 2]
    ]

print("\t\t\t------------  append()  ---------------------\n")

# agrega elementos de la lista

""" nombres = []

for usuario in usuarios:
    nombres.append(usuario[0])
print(nombres) """



# es lo mismo del anterior
""" nombres1 = [usuario1[0] for usuario1 in usuarios]
print(nombres1) """

# Filtrar
""" nombres = [usuario for usuario in usuarios if usuario[1] > 3]
print(nombres) """

# filtrar solo la posicion 0 (los valores string)
""" nombres = [usuario[0] for usuario in usuarios if usuario[1] > 3]
print(nombres) """

print("\t\t\t------------  map() y filter() ---------------------\n")

#nombre1 = list(map(lambda usuario : usuario[0], usuarios))
menosUsuarios = list(filter(lambda usuario : usuario[1] > 2, usuarios))
print(menosUsuarios)
