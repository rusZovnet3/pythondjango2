import math             # libreria



print("=============  números funciones =============\n")

print("\n\t\t------------------ round() ---------")
# redondea el numero con el decimal
print(f"round(7.89)  ===>  {round(7.89)}")


print("\n\t\t------------------ abs() ---------")
# devuelve el numero positivo
print(f"abs(11.89)  ===>  {abs(11.89)}")
print(f"abs(-7.89)  ===>  {abs(-7.89)}")



print("\n=============================================\n===========   Libreria math  ================\n=============================================")

print("\n------------- .ceil() -------------\n")
# el numero entero mas cercano
print(f"math.ceil(1.4)   ==== >  {math.ceil(1.4)}")


print("\n------------- .floor() -------------\n")
# el numero entero mas cercano hacia abajo
print(f"math.floor(3.6899)   ==== >  {math.floor(3.6899)}")


print("\n------------- .isnan() -------------\n")
alpha = "hol"
# verifica que no es numero
print(f"math.isnan(3.6899)   ==== >  {math.isnan(3.6899)}")
print(f"str(math.isnan(25))   ==== >  {str(math.isnan(25))}")
print(f"math.isnan(False)   ==== >  {math.isnan(False)}")


print("\n------------- .pow() -------------\n")
# a ^ b
print(f"math.pow(3,3)   ==== >  {math.pow(3,3)}")


print("\n------------- .sqrt() -------------\n")
# la raiz cuadrada
print(f"math.sqrt(144)   ==== >  {math.sqrt(144)}")



