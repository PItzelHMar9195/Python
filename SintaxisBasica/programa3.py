"""
* Crea un programa que reciba tu edad y tu 
* año de nacimiento y calcule si estos son 
* consistentes.
"""

#Mensaje de bienvenida
print("\n\n\t\t**** ¿TU EDAD COINCIDE? ****\n")

#Lectura dw datos
edad = int(input("\t\tINGRESA TU EDAD: "))
anio = int(input("\t\tINGRESA TU AÑO DE NACIMIENTO: "))

#Se valida que coincida la edad y el año
if 2024 - anio == edad:
  print("\n\t\t¡SÍ COINCIDEN!\n")
else:
  print("\n\t\t¡NO COINCIDEN!\n")
