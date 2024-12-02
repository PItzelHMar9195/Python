"""
* Escribe un programa que reciba un número
* y muestre si es par o impar.
"""

#Mensaje
print("\n\n\t\t**** ¿ES PAR O IMPAR? ****\n")

#Lectura de datos
numero = int(input("\t\tINGRESA UN NÚMERO: "))

#Se determina si es par o no
if numero % 2 == 0:
  print(f"\n\t\tEL NÚMERO ({numero}) ES PAR\n")
else:
  print(f"\n\t\tEL NÚMERO ({numero}) ES IMPAR\n")