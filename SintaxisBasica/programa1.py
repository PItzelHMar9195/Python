"""
* Escribe un programa que solicite tu nombre y tu 
* ciudad de residencia, luego imprímelo en una sola 
* frase.
"""

#Mensaje de bienvenida
print("\n\n\t\t**** PRESENTACIÓN ****\n")

#Lectura de datos
name = input("\t\t¡HOLA! ¿CUÁL ES TU NOMBRE? ")
city = input("\t\tY, ¿DE DÓNDE ERES? ")

#Se imprime el mensaje
#print("\t\tNice to meet you",name, "Really, I'm from", city, "too!")
print(f"\n\t\t¡MUCHO GUSTO {name}! ¡{city} ES UN LINDO LUGAR!\n")