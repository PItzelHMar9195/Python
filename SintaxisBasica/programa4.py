"""
* Escribe un programa que convierta grados 
* Celsius a Fahrenheit.
"""

#Mensaje de bienvenida
print("\n\n\t\tConvserión de gados C° a F")

#Lectura de datos
gradosC = int(input("\t\tIngresa la temperatura a convertir: "))

#Se muestra la conversión

#Método 1
gradosF = (gradosC * 1.8) + 32
print("\t\tLa temperatura en Fahrenheit es", gradosF)

#Método 2
print("\t\tLa temperatura en Fahrenheit es", (gradosC * 1.8) + 32)