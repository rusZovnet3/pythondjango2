print("\n==========  diccionarios  ====================\n")

print("sintaxi de diccionario")
print("variable = {'variable string': cualquier typo de valor}")


print("\n\t\t\t------------    -------------\n")

dic1 = {"x": 25, "y": 50}

#print(dic1)
#print(dic1["x"])
#print(dic1["y"])

print("\n\t\t\t------------  para agregar un elemento  -------------\n")
# se agregar al final de los elementos

dic1["z"] = 14
#print(dic1)

#print(dic1.get("x"))    # muestra el valor
#print(dic1.get("a"))    # muestra None que no existe
print(dic1.get("b", 45))    # muestra que no existe, pero muestra un valor por defecto

print("\n\t\t\t------------  eliminar un elemento  -------------\n")
# elimina la variable y su valor

del dic1["y"]
print(dic1)

del (dic1["x"])
print(dic1)


dic1["x"] = 33
dic1["p"] = "Hola"
dic1["py"] = 15.85

print("\n\t\t\t------------   -------------\n")

for valor in dic1:
    #print(valor)
    print(valor, dic1[valor])

print("\n\t\t\t------------ mostrando Tuplas  -------------\n")

# convirtiendo de diccionario a Tuplas
for valor1 in dic1.items():
    print(valor1)


print("\n\t\t\t------------ Desempaquetados Tuplas  -------------\n")

for llave, valor2 in dic1.items():
    print(llave, valor2)


print("\n\t\t\t------------   -------------\n")

usuarios = [
    {"id": 1, "nombre": "Maria Victoria", "carrera": "Ing Comercial", "sueldo": 2500},
    {"id": 2, "nombre": "Carmen Rosa", "carrera": "Ing Comercial", "sueldo": 1500},
    {"id": 3, "nombre": "Ana Karen", "carrera": "Ing Sistemas", "sueldo": 1300},
    {"id": 4, "nombre": "Gregoria", "carrera": "Contaduria Publica", "sueldo": 3500},
    {"id": 5, "nombre": "Gricelda", "carrera": "Ing Industrial", "sueldo": 2500},
    {"id": 6, "nombre": "Lurdes", "carrera": "Contaduria Publica", "sueldo": 4000},
    {"id": 7, "nombre": "Gabriela", "carrera": "Farmaceutica", "sueldo": 2500},
    {"id": 8, "nombre": "Rosio", "carrera": "Educadora", "sueldo": 3000},
    {"id": 9, "nombre": "Cristhina", "carrera": "Medicina", "sueldo": 4500},
    {"id": 10, "nombre": "Jessica", "carrera": "Ing Sistemas", "sueldo": 2500}
]


# mostrar sus valores de la llave nombre
for usuario in usuarios:
    print(usuario["nombre"])
