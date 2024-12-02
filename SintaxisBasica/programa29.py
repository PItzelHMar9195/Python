"""
* Crea un programa que solicite un número y 
* muestre su tabla de multiplicar.
"""

#Mensaje
print("\n\t\t\t**** TABLAS DE MULTIPLICAR ****\n")

#Lectura del dato
numero = float(input("\t\tINGRESA UN NÚMERO: "))

#Se muestra la tabla de multiplicar
print("\n")
for i in range(11):
  print(f"\t\t{numero} * {i} = {numero * i}")
print("\n")