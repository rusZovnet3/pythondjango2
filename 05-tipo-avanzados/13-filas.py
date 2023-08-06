from collections import deque

print("\n==========  filas  ====================\n")

fila = deque([3, 5, 1, 2])

fila.append(7)
fila.append(4)
fila.append(6)

print(fila)

print("\n\t\t---------- eliminar elemento  -----------\n")
# eliminar elelmento a la izquierda
# elimina un elemento inicial
print(fila)
fila.popleft()
print(fila)


print("\n\t\t----------   -----------\n")
print(f"fila1 = deque([3, 5]")

fila1 = deque([3, 5])
fila1.popleft()
fila1.popleft()


if not fila1:
    print("Fila vacia")






