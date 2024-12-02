"""
* Escribe un programa que reciba tres números
* y muestre el mayor y el menor.
"""

#Mensaje
print("\n\n\t\t**** ¿QUÉ NÚMERO ES MAYOR? ****\n")
#Lectura de datos
valorA = float(input("\t\tINGRESA EL VALOR A: "))
valorB = float(input("\t\tINGRESA EL VALOR B: "))
valorC = float(input("\t\tINGRESA EL VALOR C: "))

#Se comparan
if valorA > valorB and valorA > valorC:
  print(f"\n\t\tEL NÚMERO MAYOR ES: {valorA}")
  if valorB > valorC:
    print(f"\t\tEL NÚMERO MENOR ES: {valorC}\n")
  else:
    print(f"\t\tEL NÚMERO MENOR ES: {valorB}\n")
elif valorB > valorA and valorB > valorC:
  print(f"\n\t\tEL NÚMERO MAYOR ES: {valorB}")
  if valorA > valorC:
    print(f"\t\tEL NÚMERO MENOR ES: {valorC}\n")
  else:
    print(f"\t\tEL NÚMERO MENOR ES: {valorA}\n")
else :
  print(f"\n\t\tEL NÚMERO MAYOR ES: {valorC}")
  if valorA > valorB:
    print(f"\t\tEL NÚMERO MENOR ES: {valorB}\n")
  else:
    print(f"\t\tEL NÚMERO MENOR ES: {valorA}\n")