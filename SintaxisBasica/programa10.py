"""
* Escribe un programa que reciba un número decimal 
* y lo convierta a entero.
"""

#Mensaje
print("\n\n\t\t**** CONVERSIÓN A NÚMERO ENTERO ****\n")

#Lectura de datos
numero = float(input("\t\tINGRESA UN NÚMERO (DECIMAL): "))

#Usando división entera
#Método 1
print(F"\n\t\tEL NÚMERO ENTERO ES: {int(numero // 1)}\n")
