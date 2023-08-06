print("\n==========  agregar/eliminar - lista  ====================\n")

chicas = [
    "Jessica", "Carmen Rosa", "Gregoria", 
    "Lurdes", "Rosmery", "Rosio", 
    "Jimena", "Yanine", "Lurdes", 
    "Carmen Evelin", "Anahi", "Lurdes", 
    "Jimena", "Yussara", "Jenny", 
    "Karen", "Anahi", "Rosario", 
    "Maria Victoria", "Daniela", "Yolanda", 
    "Monica", "Gabriela", "Rosmery", "Lurdes"
    ]

print("\n\t\t\t-------------  agregar elemento  --------------\n")

#  inserta elemnto, dependiendo la psocision

""" chicas.insert(1, "Yanine")
print(chicas) """

#  Inserta elemento a la ultima posicion, con posicion penultimo actual
#chicas.insert(-1, "Briyith")

#  Inserta elemento a la ultima posicion
""" chicas.append("Ana Karen")
print(chicas)
print(chicas[3]) """



print("\n\t\t\t-------------  eliminar elemento  --------------\n")

# elimina el primer elemento de la izquierda de la lista
""" chicas.remove("Lurdes")
print(chicas)
print(chicas[3]) """



""" chicas.remove("Lurdes")
chicas.pop(1)
print(chicas) """


# eliminar elemento por indice

""" del chicas[3]
print(chicas) """

# limpiar los elementos de la lista
chicas.clear()
print(chicas)


