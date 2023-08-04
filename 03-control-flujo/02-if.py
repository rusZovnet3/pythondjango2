print("=============  Condicion if , else, elif =============\n")

edad = input("Ingresa tu edad : ")

edad = int(edad)

if edad < 18:
    if edad >= 8 and edad <= 17:
        print(f"Puedes ver peliculas de series animados")
    else:
        if edad < 8:
            print("No pueden entrar por menores de edad")
else:
    if edad >= 18 and edad <= 30:
        print("Tienes acceso a ver todas las peliculas")
    elif edad > 30 and edad < 60:
        print("solo pueden ver peliculas con descuentos")
    elif edad >= 60:
        print("Entrada Gratuito")
            
print("Listo")



