"""
* Haz un programa que reciba un número y 
* muestre el valor absoluto de la diferencia
* entre ese número y 100.
"""

#Mensaje
print("\n\n\t\t**** Calculadora de valor absoluto ****\n")

#Lectura de datos
numero = float(input("\t\tINGRESA UN NÚMERO: "))

#Se realiza el cálculo
if numero - 100 > 0:
  print(f"\n\t\t|{numero} - 100| = |{numero - 100}| = {numero - 100}\n")
else:
  print(f"\n\t\t|{numero} - 100| = |{numero - 100}| = {(numero - 100) * -1}\n")