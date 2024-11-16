"""
* Crea un programa que reciba tu edad y tu año de 
* nacimiento y calcule si estos son consistentes.
"""

#Mensaje de bienvenida
print("\n\n\t\tCalculadora de edades")

#Lectura dw datos
edad = int(input("\t\tIngresa tu edad: "))
anio = int(input("\t\tIngresa el año de nacimiento: "))

#Se valida que sea real su edad

#Método 1
if 2024 - anio == edad:
  print("\t\tTu edad si coincide con el año de nacimiento.")
else:
  print("\t\tNo coincide tu edad con el año de nacimiento.")

#Método 2 
#Se usa una variable que calcula la edad primero
edadVerificada = 2024 - anio

if edadVerificada == edad:
  print("\t\tTu edad si coincide con el año de nacimiento.")
else:
  print("\t\tNo coincide tu edad con el año de nacimiento.")
