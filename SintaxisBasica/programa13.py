"""
* Solicita tu nombre y apellido, luego 
* imprime las iniciales en mayúsculas.
"""

#Mensaje
print("\n\n\t\t**** ESCRIBIENDO MAYÚSCULAS ****\n")

#Lectura de datos
nombre = input("\t\tINGRESA TU NOMBRE: ")
apellido = input("\t\tINGRESA TU APELLIDO: ")

print(f"\n\t\tLAS INICIALES PARA NOMBRE: {str.upper(nombre[0])} Y APELLIDO: {str.upper(apellido[0])}\n")