"""
* Crea un programa que calcule el perímetro 
* y área de un círculo solicitando su radio.
"""

#Se importan las bibliotecas
import math

#Mensaje
print("\n\n\t\tCalculadora de área y perímetro de un círculo")

#Lectura de datos
radio = int(input("\t\tIngresa el radio del círculo: "))

#Cálculo del área
#Método 1
print("\t\tEl área del círculo es: ", math.pi * (radio ** 2))

#Método 2
area = math.pi * (radio ** 2)
print("\t\tEl área del círculo es: ", area)

#Cálculo del perímetro
#Método 1
print("\t\tEl perímetro del círculo es: ", math.pi * radio * 2)

#Método 2
perimetro = math.pi * radio * 2
print("\t\tEl perímetro del círculo es: ", perimetro)