print("=============  practica calculadora =============\n")

numero1 = input("Ingresa el primer Número: ")
numero2 = input("Ingresa el segundo Número: ")

numero1 = int(numero1) 
numero2 = int(numero2)



mensaje = f"""
el resultado de la suma            {numero1} + {numero2} = {numero1 + numero2}
el resultado de la resta           {numero1} - {numero2} = {numero1 - numero2}
el resultado de la multiplicasion  {numero1} * {numero2} = {numero1 * numero2}
el resultado de la division        {numero1} / {numero2} = {numero1 / numero2}
"""


print(mensaje)

