"""
* Crea un programa que solicite tres números y calcule su promedio.
"""

#Mensaje
print("\n\n\t\tCalculadora de promedios")

#Lectura de datos
numero1 = int(input("\t\tDigita el valor del número 1: "))
numero2 = int(input("\t\tDigita el valor del número 2: "))
numero3 = int(input("\t\tDigita el valor del número 3: "))

#Se realiza el promedio
#Método 1
promedio = (numero1 + numero2 + numero3) / 3
print("\t\tEl promedio es: ", promedio)

#Método 2
print("\t\tEl promedio es: ", (numero1 + numero2 + numero3) / 3)