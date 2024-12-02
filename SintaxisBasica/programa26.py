"""
* Haz un programa que solicite un número de cuatro cifras
* y calcule la suma de sus dígitos.
"""

#Mensaje
print("\n\n\t\t**** SUMA DE NÚMEROS ****\n")

#Lectura de datos
numero = input("\t\tDIGITA UN NÚMERO DE 4 CIFRAS: ")

#Se realiza la suma
print(f"\n\t\tLA SUMA DE LOS DÍGITOS ES: {int(numero[0]) + int(numero[1]) + int(numero[2]) + int(numero[3])}")