print("\n==========  colas  ====================\n")

pila = []

pila.append(4)
pila.append(1)
pila.append(2)

print(pila)

print("\n\t\t-----------  pop()  ------------")

# retorna el ultimo elemento

ultimo = pila.pop()
print(ultimo)

print(pila)  # muestra los elementos, sin el valor retornado

print("\n\t\t-----------    ------------")
# mostrar el valor ultimo

print(pila[-1])

print("\n\t\t-----------    ------------")
pila1 = pila

print(f"pila1 = {pila1}")
pila1.pop()
pila1.pop()




if not pila1:
    print("Pila Vacia")



