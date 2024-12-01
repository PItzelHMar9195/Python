"""
* Haz un programa que reciba un nombre y edad, luego 
* imprima un mensaje que indique cuántos años le 
* faltan para cumplir 100.
"""

#Mensaje
print("\n\n\t\t**** A TI, ¿CUÁNTO TE FALTA PARA CUMPLIR 100 AÑOS? ****\n")
#Lectura de datos
nombre = input("\t\t¿CÓMO TE LLAMAS? ")
edad = int(input("\t\t¿CUÁNTOS AÑOS TIENES? "))

#Se muestra el mensaje
print(f"\n\t\t{nombre} TE FALTAN {100 - edad} AÑOS PARA CUMPLIR 100")
print("\t\t¡ES UNA LOCURA! :D\n")