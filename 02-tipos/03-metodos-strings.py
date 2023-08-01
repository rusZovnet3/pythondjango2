print("=============  metodos strings =============")

nombre = "MarIa VictoRia oreLLana MeYui"
nom = " Lurdes   Calderon   "

print("\n\t\t\t-------- upper() ---------")
print(nombre.upper())


print("\n\t\t\t-------- lower() ---------")
print(nombre.lower())

print("\n\t\t\t-------- capitalize() ---------")
# la tranbsforma la primera letra en mayuscula y el resto minuscula
print(nombre.capitalize())

print("\n\t\t\t-------- title() ---------")
print(nombre.title())

print("\n\t\t\t-------- strip() ---------")
# elimina los espaciados de derecha y izquierda
print(nom.strip())

print("\n\t\t\t-------- }() ---------")
print(nom.strip().capitalize())


print("\n\t\t\t-------- lstrip() ---------")
# elimina los espaciados de izquierda
print(nom.lstrip())


print("\n\t\t\t-------- rstrip() ---------")
# elimina los espaciados de derecha
print(nom.rstrip())


print("\n\t\t\t-------- find() ---------")
# busca el dato y devuelve la posicion
print(nombre.find("or"))


print("\n\t\t\t-------- replace(buscar,reemplazar) ---------")
print(nombre.replace("i", "y"))

print("\n\t\t\t-------- in ---------")
# busca el dato y devuelve dato boolean
print("cto" in nombre)

print("\n\t\t\t-------- in not ---------")
" no se encuentra la busqueda ?, devuelve dato boolean"
print("cto" not in nombre)
