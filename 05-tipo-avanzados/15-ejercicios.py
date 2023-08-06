from pprint import pprint

print("\n==========  Practica  ====================\n")

""" 1. Eliminar los espacios en blanco de un string y devolver una lista con los caracteres restantes.
2. Contar en un diccionario cuanto se repiten los caracteres de un string.
3. Ordenar la llaves de un diccionario por el valor que tienen y devolver una lista que contiene tuplas [("a", 3), ("b", 2), ("c", 4), ("d", 4)] 
4. de un listado de tuplas, devolver las tuplas que tengan el mayor valor.
 [("a", 3), ("b", 2), ("c", 4), ("d", 4)] => [("c", 4), ("d", 4)]
 
5. Crear un mensaje que diga:
    los caracteres que más se repiten con 4 repeticiones son: 

    -C 
    -D 

6. Juntar la solucion de los ejercicios anteriores para encontar los caracteres que más se repiten de un string.    

"""

print("\n---  1. Eliminar los espacios en blanco de un string y devolver una lista con los caracteres restantes.  ----\n")

string = "practicando python desde cero a intermedio con sintaxis distinto a OtrOs lenguaje de programacion"

def quitar_espacio(texto):
    return [char for char in texto if char != " "]  # []  devuelve en una lista

sin_espacios = quitar_espacio(string)
print(sin_espacios)

print("\n---  2. Contar en un diccionario cuanto se repiten los caracteres de un string.  ----\n")

def cuenta_caracteres(lista):
    chars_dict = {}
    for char in lista:
        if char in chars_dict:     # existe el caracter en el diccionario?
            chars_dict[char] += 1  # itera suma del caracter, luego guarda el 'caracter' en el diccionario  con su = valor
        else:
            chars_dict[char] = 1   # guarda el 'caracter' en el diccionario  con su = valor
    return chars_dict

contados = cuenta_caracteres(sin_espacios)
pprint(contados, width=1)

# from pprint import pprint    metodo para mostrar de forma Vertica (linea parado)

print('\n--- 3. Ordenar la llaves de un diccionario por el valor que se repiten al comienzo que tienen y devolver una lista que contiene tuplas\n [("a", 3), ("b", 2), ("c", 4), ("d", 4)]  ----\n')

def ordena(dict):
    return sorted(
        dict.items(),  # convertiendo los item del diccionario "b": 2 a tupla  ("b", 2) dentro de la lista
        key=lambda key : key[1],   #  ordenar por el segundo valor de la tupla
        reverse=True
    )

ordenanados = ordena(contados)
pprint(ordenanados)


print('\n--- 4. de un listado de tuplas, devolver las tuplas que tengan el mayor valor [("a", 3), ("b", 2), ("c", 4), ("d", 4)] => [("c", 4), ("d", 4)]  ----\n')

def mayores_tuplas(lista):
    maximo = lista[0][1]                    # valor asignado
    respuesta = {}                          # 
    for orden in lista:                     # desglosa la lista
        if maximo > orden[1]:               # lista[0][1]  > lista[1]
            break
        respuesta[orden[0]] = orden[1]      # la variable con su dato maximo
    return respuesta                        # mostrando la variable con mayor numero

mayores = mayores_tuplas(ordenanados)
print(mayores)

print('\n---  5. Crear un mensaje que diga: \nlos caracteres que más se repiten con 4 repeticiones son: \n\t\t-C\n\t\t-D   \n----\n')

def crea_mensaje(diccionario):
    mensaje = "Los que más se repiten son: \n"
    for key, valor in diccionario.items():   # desempaquetando item del dic
        mensaje += f"- {key} con {valor} repeticiones \n"
    return mensaje
        
mensaje = crea_mensaje(mayores)
print(mensaje)