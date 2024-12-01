"""
* Crea un programa que reciba dos números 
* y muestre el mayor de ellos.
"""

#Mensaje
print("\n\n\t\t**** ¿QUÉ NÚMERO ES MAYOR? ****\n")

#Lectura de datos
valorA = float(input("\t\tINGRESA EL VALOR A: "))
valorB = float(input("\t\tINGRESA EL VALOR B: "))

#Se comparan
if valorA > valorB :
  print(f"\n\t\t{valorA} ES MAYOR QUE {valorB}\n")
elif valorB > valorA :
  print(f"\n\t\t{valorB} ES MAYOR QUE {valorA}\n")
else :
  print("\n\t\tAMBOS VALORES SON IGUALES\n")