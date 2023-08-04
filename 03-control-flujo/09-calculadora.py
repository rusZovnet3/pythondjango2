print("\t\t\t============= calculadora  =============\n")

print("Para salir, escribe salir")
print("Las operaciones son suma, resta, multi y div")

resultado = ""

while True:
    if not resultado:
        resultado = input("Ingrese Número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingrese la Operación: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingrese siguiente número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)
    
    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        if n2 > 0:
            resultado /= n2
        else:
            print(f"No se puede dividir entre {n2}")
            break
    else:
        print("Operación no valida")
    print(f"El resultado es: {resultado}")
