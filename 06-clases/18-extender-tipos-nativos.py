print("\n==========  Extendiendo tipos nativos  ====================\n")

""" lista = list([1, 2, 3, 4])

lista.append(5)       # inserta al final
lista.insert(0, 9)    # Inserta al inicio
lista.insert(3, 7)      # la posicion, el dato
print(lista) """


class Lista(list):
    def prepend(self, item):
        self.insert(0, item)
        
lista = Lista([1, 2, 3, 4])
lista.append(5)
lista.prepend(45)

print(lista)
