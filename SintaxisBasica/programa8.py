"""
* Escribe un programa que intercambie los valores 
* de dos variables ingresadas.
"""

#Mensaje
print("\n\n\t\t**** INTERCAMBIANDO VALORES ****\n")

valorA = input("\t\tINGRESA EL PRIMER VALOR: ")
valorB = input("\t\tINGRESA EL SEGUNDO VALOR: ")

#Se intercambian valores
auxiliar = valorA
valorA = valorB
valorB = auxiliar

print(f"\n\t\tAHORA EL PRIMER VALOR ES: {valorA}")
print(f"\t\tAHORA EL SEGUNDO VALOR ES: {valorB}\n")