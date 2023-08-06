print("\n==========  Desempaquetar Listas  ====================\n")

chicas = ["Jessica", "Carmen Rosa", "Gregoria", "Lurdes", "Rosmery", "Rosio", "Jimena", "Yanine"]

# enumerar los elementos

""" for chica in enumerate(chicas):
    #print(chica)
    #print(chica[0])
    print(chica[1]) """
    
    
primer, segundo = [1, 2]   #  indice = valores , chica = valores
for indice, chica in enumerate(chicas):
    print(indice, chica)