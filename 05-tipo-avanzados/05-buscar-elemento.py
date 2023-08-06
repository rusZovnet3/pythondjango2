print("\n==========  Buscar elemento - lista  ====================\n")

chicas = ["Jessica", "Carmen Rosa", "Gregoria", "Lurdes", "Rosmery", "Rosio", "Jimena", "Yanine", "Lurdes", "Carmen Evelin", "Anahi", "Lurdes", "Jimena", "Yussara", "Jenny", "Karen"]

# busca el elemento y devuelve la posicion
#print(chicas.index("Rosmery"))


# Buscar las veces que hay el elemento
print(f"Se repite {chicas.count('Lurdes')} veces")

if "Lurdes" in chicas:
    print(f"posicion: {chicas.index('Lurdes')}\n")

