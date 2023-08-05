print("\n========================  Depuración de funciones =================================")

# Usando depuracion del vc

def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado

print("Prueba")
re = largo("Python console")
print(re)