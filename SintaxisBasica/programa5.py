"""
* Crea un programa que calcule el perímetro 
* y área de un círculo solicitando su radio.
"""

#Se importan las bibliotecas
import math

#Mensaje
print("\n\n\t\tÁREA Y PERÍMETRO DE UN CÍRCULO\n")

#Lectura de datos
radio = int(input("\t\tINGRESA EL RADIO: "))

#Cálculo del área
print(f"\n\t\tEL ÁREA ES: {math.pi * (radio ** 2)}")

#Cálculo del perímetro
print(f"\t\tEL PERÍMETRO ES: {math.pi * radio * 2}\n")
