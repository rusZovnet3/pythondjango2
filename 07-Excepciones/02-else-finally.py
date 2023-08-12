print("\n==========  else - finally  ====================\n")

""" ------- else:
se ejecuta cuando no exista errores

----- finally:
se ejecuta por los dos lados, tenga ó no tenga errores
. """



""" try:
    n1 = int(input("Ingrese primer números: "))
except Exception as e:
    print("Ocurrio un error")
else:
    print("No ocurrio ningun error") """


try:
    n1 = int(input("Ingrese primer números: "))
except Exception as e:
    print("Ocurrio un error")
else:
    print("No Ocurrio ningun error")
finally:
    print("se ejecuta siempre")
