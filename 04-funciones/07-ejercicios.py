print("\n========================  practica =================================")

''' 
palabra al reves
ejemplo:
arroz  =   zorra ==> No
oruro  = oruro   ==>  si
reconocer = reconocer  ==> sí


'''

def no_space(texto):
    nuevotexto = ""
    for char in texto:
        if char != " ":
            nuevotexto += char
    return nuevotexto
     
def reverse(texto):
    texto_reves = ""
    for char in texto:  # desglosa del 1er al n
        texto_reves = char + texto_reves
    return texto_reves

def es_palindromo(texto):
    texto = no_space(texto)
    reves = reverse(texto)
    return texto.lower() == reves.lower()


print(es_palindromo("Amo la palOma"))
print(es_palindromo("hOlA"))

""" print("Oruro", es_palindromo("Oruro"))
print("REconocer", es_palindromo("reconocer"))

print("Python", es_palindromo("Python"))
print("ABBa", es_palindromo("aBBA")) """