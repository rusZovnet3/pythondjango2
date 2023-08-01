print("============  STRING  ============\n")
dato = "Ultimate Python"
dato1 = """
Lo ultimo de Python,
este curso contempla todos las sintaxis,
que necesitas aprender para,
encontar un trabajo como programador.

"""

print("\t\t-----  simple  ------\n")
print(dato)

print("\t\t-----  multiple lineas  ------")
print(dato1)


print("\t\t-----  metodo len() - cantidad de caracter en la variable  ------")
print("dato = 'Ultimate Python'")
print("dato2 = len(dato) ===> " + str(len(dato)))

print("\n\t\t\t\t-----  mostrar la variable de la posicion  ------")
print(dato[9])

print("\t\t-----  mostrar la posicion del caracter  variable[:]  ------")
print("\t\tdato = 'Ultimate Python'")
print(dato[0])

print(dato[0:8])    # es igual a
print(dato[:8])     # este

print(dato[9:])

# por defecto sera 0 y la longitud
print(dato[:])

