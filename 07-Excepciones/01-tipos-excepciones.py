print("\n==========  Tipos de Excepciones  ====================\n")

""" try:
    n1 = int(input("Ingrese primer números: "))
except Exception as e:
    print(type(e)) """

""" try:
    n1 = int(input("Ingrese primer números: "))
    sdfsd   # omite error de linea
except Exception as e:
    print(type(e)) """


# ValueError
# True  === > identifica el error no asignada
# False === > omite los errores de linea, muestra el mensaje del except

# NameError
# evita los errores de linea no asignada
# muestra el mensaje dl error elegante


try:
    n1 = int(input("Ingrese primer números: "))
    sdfsd
except ValueError as e:
    print("Ingrese un valor que corresponda")
except NameError as e:
    print("Ocurrio un error inesperado")