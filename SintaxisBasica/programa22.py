"""
* Crea un programa que reciba el largo de los lados
* de un triángulo y calcule su área con la fórmula de Herón.
"""

import math

print("\n\n\t\t**** USANDO LA FÓRMULA DE HERÓN ****\n")

#Lectura de datos
valor1 = float(input("\t\tDIGITA EL LARGO DEL PRIMER LADO: "))
valor2 = float(input("\t\tDIGITA EL LARGO DEL SEGUNDO LADO: "))
valor3 = float(input("\t\tDIGITA EL LARGO DEL TERCER LADO: "))

#Se calcula primero el semiperímetro:
s = (valor1 + valor2 + valor3) / 2
s = s * (valor1 - s) * (valor2 - s) * (valor3 - s)

print(f"\t\tEL ÁREA DEL TRIÁNGULO ES: {math.sqrt(s)}")