"""
* Escribe un programa que reciba tres notas de 
* un estudiante y calcule su promedio.
"""

print("\n\n\t\t**** CALCULADORA DE PROMEDIOS ****\n")

#Lectura de datos
numero1 = float(input("\t\tINGRESA LA PRIMER NOTA: "))
numero2 = float(input("\t\tINGRESA LA SEGUNDA NOTA: "))
numero3 = float(input("\t\tINGRESA LA TERCER NOTA: "))

#Se calcula el promedio
#Método 2
print(f"\n\t\tEL PROMEDIO ES: {(numero1 + numero2 + numero3) / 3}\n")