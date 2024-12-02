"""
* Haz un programa que reciba una cantidad en segundos
* y la convierta a horas, minutos y segundos.
"""

print("\n\n\t\t**** CONVERSIÓN DE TIEMPO ****\n")

#Lectura de datos
segundos = int(input("\t\tINGRESA LOS SEGUNDOS: "))

print(f"\n\t\tHORAS: {segundos // 3600} MINUTOS: {(segundos % 3600) // 60} SEGUNDOS: {segundos % 60}\n")