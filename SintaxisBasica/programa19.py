"""
* Crea un programa que solicite tu peso y altura,
* y calcule tu índice de masa corporal (IMC).
"""

#Mensaje
print("\n\n\t\t**** Calculadora de IMC")

#Lectura de datos
peso = float(input("\t\tINGRESA TU PESO: "))
altura = float(input("\t\tINGRESA TU ALTURA: "))

#Se calcula el IMC
print(f"\n\t\tTU IMC ES: {peso / (altura ** 2)}\n")